from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from utils import extract_features # Dùng chung hàm với file Train

app = FastAPI()

# Load mô hình đã train lại
model = joblib.load("models/rf_model.pkl")

class Payload(BaseModel):
    sentence: str

@app.post("/predict")
async def predict(data: Payload):
    # 1. Trích xuất đặc trưng từ payload gửi lên
    features = extract_features(data.sentence)
    
    # 2. Dự đoán xác suất
    # Dùng predict_proba để lấy độ tin cậy, giúp chặn nhạy hơn
    prediction_prob = model.predict_proba([features])[0]
    is_attack_prob = prediction_prob[1]
    
    threshold = 0.3 
    is_attack = 1 if is_attack_prob > threshold else 0
    
    return {
        "sentence": data.sentence,
        "is_attack": is_attack,
        "confidence": float(is_attack_prob),
        "details": {
            "entropy": features[0],
            "special_ratio": features[2]
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

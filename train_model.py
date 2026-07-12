import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from utils import extract_features # Import hàm từ file trên

# 1. Load dữ liệu đã gộp (Cả SQLiV3 và OWASP bypass)
df = pd.read_csv("SQLiV3_cleaned_balanced.csv")
df['Sentence'] = df['Sentence'].fillna("empty")

# 2. Trích xuất đặc trưng cho toàn bộ tập dữ liệu
print("Đang trích xuất đặc trưng...")
X = [extract_features(text) for text in df['Sentence']]
y = df['Label']

# 3. Chia tập Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Huấn luyện Random Forest
print("Đang huấn luyện mô hình...")
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 5. Lưu mô hình
joblib.dump(model, "models/rf_model.pkl")
print("Đã lưu mô hình mới tại models/rf_model.pkl")
print(f"Độ chính xác trên tập Test: {model.score(X_test, y_test)*100:.2f}%")
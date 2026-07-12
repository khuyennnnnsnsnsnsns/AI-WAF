import pandas as pd

# 1. Đọc danh sách payload từ file txt
with open('owasp_bypass.txt', 'r', encoding='utf-8') as f:
    owasp_payloads = [line.strip() for line in f if line.strip()]

# 2. Tạo DataFrame mới cho dữ liệu OWASP
df_owasp = pd.DataFrame({
    "Sentence": owasp_payloads,
    "Label": [1] * len(owasp_payloads)
})

# 3. Đọc file CSV đã có của bạn
try:
    df_old = pd.read_csv("SQLiV3_cleaned_balanced.csv")
    # Gộp 2 dữ liệu lại
    df_final = pd.concat([df_old, df_owasp], ignore_index=True)
    
    # Xóa trùng lặp (nếu có) để dữ liệu sạch nhất
    df_final = df_final.drop_duplicates(subset=["Sentence"])
    
    # Lưu lại file CSV
    df_final.to_csv("SQLiV3_cleaned_balanced.csv", index=False)
    print(f"Thành công! Đã thêm {len(df_owasp)} mẫu bypass từ OWASP vào Dataset.")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file SQLiV3_cleaned_balanced.csv")
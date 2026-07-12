#Dữ liệu ban đầu khi chưa chỉnh sửa
import pandas as pd

dataset = pd.read_csv("SQLiV3.csv")
df = pd.DataFrame(dataset)
print(df)
print("----------------------------------------------------------------------")
print(df.info())

#Xóa 2 cột không cần thiết
del df['Unnamed: 2']

del df['Unnamed: 3']

#Coi thông tin dữ liệu Sau khi Xóa
print(df.head())

#Kiểm tra dữ liệu có null không và kết quả cho thấy cả 2 cột đều còn dữ liệu null
import matplotlib.pyplot as plt

print(df.isna())
print(df.isna().any())

#Xóa dữ liệu null
df = df.dropna(subset=["Sentence"])
df = df[df["Sentence"].str.strip() != ""]
df = df.drop_duplicates(subset=["Sentence"])

#Coi nhãn dữ liệu
df["Label"].value_counts()

#Xóa nhãn dữ liệu khác 0 và khác 1 và dữ liệu trùng
df = df[df['Label'].isin(["0","1"])]
df = df.drop_duplicates(subset=["Sentence"])

#Chuyển kiểu dữ liệu cột label thành int64
df["Label"] = df["Label"].astype(int)

df0 = df[df["Label"] == 0]
df1 = df[df["Label"] == 1]

df0_sample = df0.sample(n=len(df1), random_state=42)

df_balanced = pd.concat([df0_sample, df1])

print(df_balanced["Label"].value_counts())

count_classes = df_balanced['Label'].value_counts(sort=True)

count_classes.plot(kind='bar', rot=0)

plt.title("Quantities of malware and normal strings")
plt.xlabel("Type")
plt.ylabel("Quantities")

plt.show()

# Xuất dữ liệu đã làm sạch và cân bằng ra file CSV
df_balanced.to_csv("SQLiV3_cleaned_balanced.csv", index=False)
print("Đã xuất file SQLiV3_cleaned_balanced.csv thành công!")
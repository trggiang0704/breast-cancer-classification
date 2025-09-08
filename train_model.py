import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# 1. Đọc dữ liệu
du_lieu = pd.read_csv("data.csv")

# 2. Xử lý dữ liệu: bỏ cột id và cột trống
du_lieu = du_lieu.drop(columns=["id", "Unnamed: 32"])

# 3. Chuyển nhãn diagnosis từ chữ sang số (M=0, B=1)
du_lieu["diagnosis"] = du_lieu["diagnosis"].map({"M": 0, "B": 1})

# 4. Chọn 5 đặc trưng quan trọng nhất
dac_trung_quan_trong = [
    "concave points_mean",
    "concave points_worst",
    "area_worst",
    "concavity_mean",
    "radius_worst"
]

X = du_lieu[dac_trung_quan_trong]
y = du_lieu["diagnosis"]

# 5. Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 6. Khởi tạo mô hình Random Forest
mo_hinh = RandomForestClassifier(
    n_estimators=100,
    max_features="sqrt",
    random_state=42
)

# 7. Huấn luyện mô hình
mo_hinh.fit(X_train, y_train)

# 8. Đánh giá mô hình
du_doan = mo_hinh.predict(X_test)
do_chinh_xac = accuracy_score(y_test, du_doan)
print(f"🎯 Độ chính xác (chỉ với 5 đặc trưng): {do_chinh_xac*100:.2f}%\n")
print("📊 Báo cáo phân loại:")
print(classification_report(y_test, du_doan, target_names=["Ác tính", "Lành tính"]))
print("🔍 Ma trận nhầm lẫn:")
print(confusion_matrix(y_test, du_doan))

# 9. Lưu mô hình và danh sách đặc trưng
joblib.dump(mo_hinh, "model.pkl")
joblib.dump(dac_trung_quan_trong, "features.pkl")

print("\n✅ Đã lưu mô hình vào file model.pkl và features.pkl")

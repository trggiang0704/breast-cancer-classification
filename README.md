# 🩺 Cancer-Classifier với Flask & Random Forest
## 📌 Giới thiệu

Đây là một ứng dụng web đơn giản để dự đoán ung thư vú dựa trên mô hình Random Forest.
Người dùng nhập 5 đặc trưng quan trọng nhất của khối u (ví dụ: concave points, area, radius…) vào giao diện web → hệ thống dự đoán khối u ÁC TÍNH hay LÀNH TÍNH ngay lập tức.

## 🛠️ Công nghệ và công cụ sử dụng  
| Thành phần        | Công nghệ sử dụng         |
|-------------------|---------------------------|
| Ngôn ngữ lập trình | Python 3                 |
| Web framework     | Flask                     |
| Machine Learning  | Random Forest (scikit-learn) |
| Xử lý dữ liệu     | pandas, scikit-learn      |
| Frontend          | HTML, CSS, bootstrap 5    |

## 🧠 Logic & hoạt động

Tiền xử lý dữ liệu:

Bỏ các cột không cần thiết (id, Unnamed: 32).

Chuyển nhãn diagnosis: M = 0 (ác tính), B = 1 (lành tính).

Huấn luyện mô hình:

Sử dụng Random Forest Classifier với 5 đặc trưng quan trọng nhất:

concave points_mean

concave points_worst

area_worst

concavity_mean

radius_worst

Triển khai Flask app:

Giao diện web gồm form nhập giá trị 5 đặc trưng.

Khi submit → Flask backend dự đoán bằng mô hình đã huấn luyện.

Kết quả hiển thị:

❌ Khối u ÁC TÍNH

✅ Khối u LÀNH TÍNH

## 🎨 Giao diện

🔹 Form nhập dữ liệu:

<img width="987" height="696" alt="image" src="https://github.com/user-attachments/assets/726bcd9e-9b08-4d81-b48f-6ac6db4c625f" />

🔹 Kết quả dự đoán:

<img width="790" height="782" alt="image" src="https://github.com/user-attachments/assets/a9b5a8d6-4943-4e51-a4fe-cfd5fee713fc" />


## 📂 Cấu trúc dự án
```bash
cancer_classify/
│── train_model.py      # Huấn luyện và lưu mô hình Random Forest
│── app.py              # Flask app để chạy web dự đoán
│── data.csv            # Dữ liệu ung thư vú
│── model.pkl           # File mô hình đã huấn luyện
│── features.pkl        # Danh sách 5 đặc trưng quan trọng
```

## 🚀 Khởi chạy ứng dụng
```bash
1. Huấn luyện mô hình
python train_model.py

2. Chạy ứng dụng Flask
python app.py

3. Mở trình duyệt
http://127.0.0.1:5000
```
## 💡 Ghi chú

Mô hình hiện tại chỉ sử dụng 5 đặc trưng quan trọng để tăng tốc độ dự đoán.

Có thể mở rộng bằng cách:

Thêm nhiều đặc trưng.

Cải thiện giao diện bằng Bootstrap/Flask-Template.

Lưu lịch sử dự đoán.

Triển khai lên Heroku/Render/Vercel để chạy online.

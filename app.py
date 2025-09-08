from flask import Flask, request, render_template_string
import joblib
import pandas as pd

# 1. Nạp mô hình và danh sách đặc trưng
mo_hinh = joblib.load("model.pkl")
dac_trung_quan_trong = joblib.load("features.pkl")

# 2. Khởi tạo Flask app
app = Flask(__name__)

# Giao diện HTML đơn giản
html_form = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Dự đoán ung thư vú</title>
    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
            min-height: 100vh;
        }
        .card {
            border-radius: 20px;
            overflow: hidden;
        }
        .card-header {
            background: linear-gradient(90deg, #1976d2, #42a5f5);
        }
        .form-label {
            color: #0d47a1;
        }
        .btn-success {
            border-radius: 10px;
            font-weight: bold;
            transition: 0.3s;
        }
        .btn-success:hover {
            background-color: #2e7d32;
            transform: scale(1.02);
        }
        .alert {
            border-radius: 10px;
            font-size: 1.1rem;
        }
    </style>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center py-5">
        <div class="card shadow-lg w-100" style="max-width: 600px;">
            <div class="card-header text-white text-center py-3">
                <h3 class="mb-0"><i class="bi bi-heart-pulse"></i> Dự đoán ung thư vú (Random Forest)</h3>
            </div>
            <div class="card-body p-4">
                <form method="post">
                    {% for ten in dac_trung_quan_trong %}
                        <div class="mb-3">
                            <label class="form-label fw-semibold">{{ ten }}</label>
                            <input type="number" step="any" name="{{ ten }}" class="form-control" placeholder="Nhập giá trị" required>
                        </div>
                    {% endfor %}
                    <button type="submit" class="btn btn-success w-100 py-2">
                        <i class="bi bi-graph-up-arrow"></i> Dự đoán
                    </button>
                </form>
                {% if ket_qua %}
                    <div class="alert alert-info mt-4 text-center fw-bold">
                        <i class="bi bi-info-circle"></i> {{ ket_qua }}
                    </div>
                {% endif %}
            </div>
            <div class="card-footer text-muted text-center">
                <small>✨ Ứng dụng demo bằng Flask + Bootstrap 5</small>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def du_doan():
    ket_qua = None
    if request.method == "POST":
        # Lấy dữ liệu từ form
        gia_tri_nhap = [float(request.form[ten]) for ten in dac_trung_quan_trong]
        du_lieu_moi = pd.DataFrame([gia_tri_nhap], columns=dac_trung_quan_trong)

        # Dự đoán
        du_doan_moi = mo_hinh.predict(du_lieu_moi)
        if du_doan_moi[0] == 0:
            ket_qua = "❌ Khối u ÁC TÍNH"
        else:
            ket_qua = "✅ Khối u LÀNH TÍNH"

    return render_template_string(html_form, dac_trung_quan_trong=dac_trung_quan_trong, ket_qua=ket_qua)

if __name__ == "__main__":
    app.run(debug=True)

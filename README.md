# 🧠 **VNStock Agent**

> Hướng dẫn cài đặt và kiểm thử API cho dự án **vnstock-agent**

---

## 🚀 1. Clone dự án

```bash
# Clone repository
git clone <repo-url> && cd vnstock_agent
```

---

## 🧩 2. Hai cách chạy và kiểm thử API

### 🖥️ Cách 1: Chạy trực tiếp trên môi trường cục bộ (Local)

#### 🔧 Bước 1: Cài đặt môi trường

```bash
# Cài đặt công cụ quản lý môi trường (uv)
pip install uv

# Tạo và đồng bộ môi trường ảo
uv sync

# Kích hoạt môi trường ảo
.venv\Scripts\activate
```

---

#### ▶️ Bước 2: Khởi chạy API

Mở **terminal thứ nhất** và chạy lệnh:

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

Sau khi khởi chạy thành công, truy cập tài liệu API tại:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

#### 🧪 Bước 3: Kiểm thử API với bộ câu hỏi có sẵn

Mở **terminal thứ hai** và chạy lệnh:

```bash
python -m test.test_api
```

**📂 Bộ câu hỏi kiểm thử** được định nghĩa sẵn trong file:
`test/test_api.py`

> File này chứa danh sách các câu hỏi mẫu giúp đánh giá khả năng phản hồi và logic của API.

---

### 🐳 Cách 2: Chạy và kiểm thử bằng **Docker Compose**

Nếu bạn muốn thử nhanh mà **không cần cài đặt môi trường**:

```bash
docker compose up
```

Sau khi chạy, quan sát log trong terminal để xem kết quả kiểm thử.

---

## ⚙️ 4. Biến môi trường

Tạo file `.env` để cấu hình khóa truy cập (ví dụ: OpenAI API key):

```bash
OPENAI_API_KEY=xxxxx
```

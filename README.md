# Vào môi trường ảo

Để **vào môi trường ảo (virtual environment)** trong thư mục `backendpython`, bạn làm theo các bước sau (áp dụng cho Windows):

### ✅ Bước 1: Mở Terminal hoặc Command Prompt

* Nếu đang dùng VS Code, bạn nhấn `Ctrl + ~` để mở terminal trong VS Code.

### ✅ Bước 2: Di chuyển vào thư mục chứa môi trường ảo

```bash
cd backendpython
```

### ✅ Bước 3: Kích hoạt môi trường ảo
tao mt ao
python -m venv venv

Nếu bạn đang dùng **Windows**:

```bash
venv\Scripts\activate
```

Nếu bạn đang dùng **Linux/Mac**:

```bash
source venv/bin/activate
```


# Khắc phục khi đổi máy

### ✅ (Tùy chọn) Nếu bạn có nhiều dependency hơn:

Nếu trên máy cũ bạn đã tạo `requirements.txt`, bạn có thể dùng:

``` bash
pip install -r requirements.txt
``` 

Nếu trên máy cũ bạn đã tạo `requirements.txt`, bạn có thể dùng:

```bash
venv\Scripts\activate
```

---

### ✅ Sau khi cài xong:

Chạy lại file `main.py` hoặc dùng `uvicorn` nếu đó là một web app FastAPI:

```bash
uvicorn main:app --reload
```

Giả sử trong `main.py` bạn có dòng:

```python
app = FastAPI()
```

---

Nếu bạn muốn mình kiểm tra luôn nội dung `main.py` hoặc tạo `requirements.txt` phù hợp, cứ gửi tiếp nội dung nhé.

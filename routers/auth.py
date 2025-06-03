from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from models.user import User
from database import SessionLocal
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["Auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = pwd_context.hash(user.password) # Mã hóa mật khẩu
    db_user = User(username=user.username, hashed_password=hashed_pw, role=user.role, email=user.email, full_name=user.full_name, phone=user.phone) # Tạo đối tượng người dùng mới
    db.add(db_user) # Thêm người dùng vào database
    db.commit() # Lưu dữ liệu vào database
    db.refresh(db_user) # Cập nhật dữ liệu vào database
    return {"msg": "User registered"} # Trả về thông báo người dùng đã đăng ký thành công

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phone == user.phone).first() # Kiểm tra xem người dùng có tồn tại không ( có nghĩa là truy vấn dữ liệu từ database )
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials") # Nếu không tồn tại hoặc mật khẩu không khớp thì trả về lỗi 401
    return {"msg": "Login successfully", "user": {
        "username": db_user.username,
        "role": db_user.role,
        "email": db_user.email,
        "full_name": db_user.full_name,
        "phone": db_user.phone
    }} # Trả về thông báo người dùng đã đăng nhập thành công

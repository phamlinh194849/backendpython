from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from models.user import User
from database import SessionLocal
from auth.jwt_handler import create_access_token
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
    hashed_pw = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_pw, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

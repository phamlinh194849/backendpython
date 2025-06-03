from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    full_name: str
    phone: str
    role: str = "customer"

class UserLogin(BaseModel):
    phone: str
    password: str

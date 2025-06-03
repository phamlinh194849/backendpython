from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:KmaalPOxZuCgcscMcNjTAiMJXYGLvoQJ@interchange.proxy.rlwy.net:57692/railway"  # Hoặc PostgreSQL URI



# Tạo engine không truyền connect_args nếu dùng PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()



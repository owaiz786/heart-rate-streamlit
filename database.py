from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://backend_rna7_user:zZFvaNnWT8BE5hHgSrsg1M8qFM2YpX8u@dpg-d43gqpuuk2gs7393bp7g-a.oregon-postgres.render.com/backend_rna7"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ This is what FastAPI is trying to import
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# Create the FastAPI app
app = FastAPI()

# CORS settings to allow requests from frontend
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Configuration
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = DeclarativeBase()

# Include your route endpoints here
@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Admin API"}

# Include your sales, inventory, and other endpoints here
# Example:
# from .crud import get_sales_data
# @app.get("/sales/")
# def get_sales():
#     return get_sales_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

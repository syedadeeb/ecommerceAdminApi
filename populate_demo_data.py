# populate_demo_data.py

from faker import Faker
from sqlalchemy.orm import Session
from models import Product, Sale
from datetime import date, timedelta
import random
from database import SessionLocal, engine

# Initialize Faker for generating fake data
fake = Faker()

# Function to generate mock product data
def generate_mock_products(db: Session, num_products=10):
    products = []
    for _ in range(num_products):
        product = Product(
            name=fake.product_name(),
            description=fake.sentence(),
            price=random.uniform(10, 1000),  # Random price between $10 and $1000
            category=fake.word()
        )
        products.append(product)
    db.add_all(products)
    db.commit()

# Function to generate mock sales data
def generate_mock_sales(db: Session, num_sales=100, num_products=10):
    products = db.query(Product).all()
    today = date.today()
    
    sales = []
    for _ in range(num_sales):
        product = random.choice(products)
        quantity = random.randint(1, 10)  # Random quantity sold between 1 and 10
        sale_date = today - timedelta(days=random.randint(1, 30))  # Random date within the last 30 days
        revenue = product.price * quantity
        sale = Sale(
            product_id=product.id,
            quantity=quantity,
            sale_date=sale_date,
            revenue=revenue
        )
        sales.append(sale)
    db.add_all(sales)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    
    # Generate mock product data (10 products by default)
    generate_mock_products(db)
    
    # Generate mock sales data (100 sales by default)
    generate_mock_sales(db)
    
    db.close()

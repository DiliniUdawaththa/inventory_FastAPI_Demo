from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Laptop", price=999.99, quantity=10, description="A high-performance laptop."),
    Product(id=2, name="Smartphone", price=499.99, quantity=20, description="A latest model smartphone."),
    Product(id=3, name="Headphones", price=199.99, quantity=15, description="Noise-cancelling headphones.")
]

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

@app.get("/products")
def get_products():
    return products


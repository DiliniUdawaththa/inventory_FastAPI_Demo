from fastapi import FastAPI
import database_models
from models import Product
from database import engine

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

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

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return {"message": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product}

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {"message": "Product updated successfully", "product": product}    
    
    return {"message": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"message": "Product deleted successfully"}
    
    return {"message": "Product not found"}

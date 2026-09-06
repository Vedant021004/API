from fastapi import FastAPI
from metadata import products

app = FastAPI()

@app.get("/get_product")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product

    return {"message": "Product not found"}
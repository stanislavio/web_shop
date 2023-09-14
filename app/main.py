from fastapi import FastAPI

from app.routers import categories, products, users


app = FastAPI()

app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(users.router, tags=["users"])


from fastapi import APIRouter
from src.users.router import router as users_router
from src.products.router import router as products_router

router = APIRouter()

router.include_router(prefix='/users', router=users_router)
router.include_router(prefix='/products', router=products_router)

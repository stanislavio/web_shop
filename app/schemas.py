from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    category_id: int


class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    hashed_password: str = Field(alias='password')


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

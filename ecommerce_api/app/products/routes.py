from fastapi import APIRouter, HTTPException

from app.products.schemas import ProductCreate, ProductUpdate
from app.products.service import ProductService


router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductService()


@router.get("/")
def get_products():
    return product_service.list_products()


@router.get("/search")
def search_products(q: str = ""):
    return product_service.search_products(q)


@router.get("/category/{category}")
def get_products_by_category(category: str):
    return product_service.filter_by_category(category)


@router.get("/{product_id}")
def get_product(product_id: int):
    product = product_service.get_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.post("/")
def create_product(product: ProductCreate):
    return product_service.create_product(product)


@router.put("/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    updated_product = product_service.update_product(product_id, product)

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@router.delete("/{product_id}")
def delete_product(product_id: int):
    deleted = product_service.delete_product(product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"deleted": True}
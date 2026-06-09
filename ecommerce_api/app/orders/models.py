from typing import Optional

from pydantic import BaseModel


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float


class Order(BaseModel):
    id: int
    user_id: int
    items: list[OrderItem]
    subtotal: float
    tax: float
    shipping: float
    total_price: float
    status: str = "pending"
    coupon_code: Optional[str] = None
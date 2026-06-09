from typing import Optional

from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    user_id: int
    items: list[OrderItemCreate]
    coupon_code: Optional[str] = None


class OrderStatusUpdate(BaseModel):
    status: str
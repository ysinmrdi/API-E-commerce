from fastapi import APIRouter, HTTPException

from app.orders.schemas import OrderCreate, OrderStatusUpdate
from app.orders.service import OrderService


router = APIRouter(prefix="/orders", tags=["Orders"])
order_service = OrderService()


@router.get("/")
def get_orders():
    return order_service.list_orders()


@router.get("/{order_id}")
def get_order(order_id: int):
    order = order_service.get_order(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.get("/user/{user_id}")
def get_user_orders(user_id: int):
    return order_service.get_user_orders(user_id)


@router.post("/")
def create_order(order_data: OrderCreate):
    order = order_service.create_order(order_data)

    if order is None:
        raise HTTPException(status_code=400, detail="Could not create order")

    return order


@router.patch("/{order_id}/status")
def update_order_status(order_id: int, data: OrderStatusUpdate):
    order = order_service.update_order_status(order_id, data.status)

    if order is None:
        raise HTTPException(status_code=400, detail="Invalid order or status")

    return order


@router.patch("/{order_id}/cancel")
def cancel_order(order_id: int):
    order = order_service.cancel_order(order_id)

    if order is None:
        raise HTTPException(status_code=400, detail="Could not cancel order")

    return order


@router.delete("/{order_id}")
def delete_order(order_id: int):
    deleted = order_service.delete_order(order_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"deleted": True}
from fastapi import APIRouter, HTTPException

from app.payments.schemas import PaymentCreate, PaymentStatusUpdate
from app.payments.service import PaymentService


router = APIRouter(prefix="/payments", tags=["Payments"])
payment_service = PaymentService()


@router.get("/")
def get_payments():
    return payment_service.list_payments()


@router.get("/{payment_id}")
def get_payment(payment_id: int):
    payment = payment_service.get_payment(payment_id)

    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment


@router.get("/order/{order_id}")
def get_payment_by_order(order_id: int):
    payment = payment_service.get_payment_by_order(order_id)

    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment


@router.get("/user/{user_id}")
def get_user_payments(user_id: int):
    return payment_service.get_user_payments(user_id)


@router.post("/")
def create_payment(payment_data: PaymentCreate):
    payment = payment_service.process_payment(payment_data)

    if payment is None:
        raise HTTPException(status_code=400, detail="Could not process payment")

    return payment


@router.post("/{payment_id}/refund")
def refund_payment(payment_id: int):
    payment = payment_service.refund_payment(payment_id)

    if payment is None:
        raise HTTPException(status_code=400, detail="Could not refund payment")

    return payment


@router.patch("/{payment_id}/status")
def update_payment_status(payment_id: int, data: PaymentStatusUpdate):
    payment = payment_service.update_payment_status(payment_id, data.status)

    if payment is None:
        raise HTTPException(status_code=400, detail="Invalid payment or status")

    return payment
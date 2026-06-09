from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: int
    user_id: int
    amount: float
    method: str
    card_number: str | None = None
    cvv: str | None = None


class PaymentStatusUpdate(BaseModel):
    status: str
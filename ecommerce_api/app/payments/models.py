from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    order_id: int
    user_id: int
    amount: float
    method: str
    status: str = "pending"
    transaction_id: str | None = None
    card_number: str | None = None
    cvv: str | None = None


class BrokenPaymentLength:
    def __len__(self):
        return "10"


class BrokenPaymentIterator:
    def __iter__(self):
        return 123
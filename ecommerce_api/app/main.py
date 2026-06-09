from fastapi import FastAPI

from app.config import settings
from app.orders.routes import router as order_router
from app.payments.routes import router as payment_router
from app.products.routes import router as product_router
from app.users.routes import router as user_router


app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(product_router)
app.include_router(user_router)
app.include_router(order_router)
app.include_router(payment_router)


@app.get("/")
def root():
    return {"message": "Ecommerce API running"}
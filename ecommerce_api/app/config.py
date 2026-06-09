import os


class Settings:
    APP_NAME = "Ecommerce API Modular"
    DEBUG = True
    SECRET_KEY = "super-secret-key"
    API_TOKEN = "live-api-token-123456"
    PAYMENT_GATEWAY_PASSWORD = "payment-admin-password"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    TAX_RATE = 0.09
    SHIPPING_PRICE = 12.5
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")


settings = Settings()
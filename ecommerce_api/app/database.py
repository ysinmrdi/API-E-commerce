from app.products.models import Product
from app.users.models import User


products_db = [
    Product(
        id=1,
        name="Laptop",
        description="Gaming laptop",
        price=1200.0,
        stock=8,
        category="electronics",
    ),
    Product(
        id=2,
        name="Phone",
        description="Smartphone",
        price=700.0,
        stock=20,
        category="electronics",
    ),
    Product(
        id=3,
        name="Headphones",
        description="Wireless headphones",
        price=150.0,
        stock=35,
        category="accessories",
    ),
    Product(
        id=4,
        name="Desk",
        description="Wooden desk",
        price=300.0,
        stock=4,
        category="furniture",
    ),
    Product(
        id=5,
        name="Chair",
        description="Office chair",
        price=180.0,
        stock=11,
        category="furniture",
    ),
]

users_db = [
    User(
        id=1,
        username="admin",
        email="admin@example.com",
        password="admin123",
        is_active=True,
    ),
    User(
        id=2,
        username="reza",
        email="reza@example.com",
        password="password123",
        is_active=True,
    ),
]

orders_db = []

payments_db = []
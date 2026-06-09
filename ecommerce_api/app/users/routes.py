from fastapi import APIRouter, HTTPException

from app.users.schemas import LoginRequest, UserCreate
from app.users.service import UserService


router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()


@router.get("/")
def get_users():
    return user_service.list_users()


@router.post("/")
def create_user(user: UserCreate):
    created_user = user_service.create_user(user)

    if created_user is None:
        raise HTTPException(status_code=400, detail="Email already exists")

    return created_user


@router.get("/{user_id}")
def get_user(user_id: int):
    user = user_service.get_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/{user_id}")
def deactivate_user(user_id: int):
    user = user_service.deactivate_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/login")
def login(data: LoginRequest):
    user = user_service.authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = user_service.create_access_token({"sub": user.username, "user_id": user.id})

    return {"access_token": token, "token_type": "bearer"}
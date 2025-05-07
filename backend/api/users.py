from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "Get all users"}

@router.post("/")
async def create_user():
    return {"message": "User created"}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Get user {user_id}"}

@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": f"Updated user {user_id}"}

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"Deleted user {user_id}"}

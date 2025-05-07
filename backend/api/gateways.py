from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/")
async def get_gateways():
    return {"message": "Get all gateway locations"}

@router.get("/{gateway_id}")
async def get_gateway(gateway_id: int):
    return {"message": f"Get gateway {gateway_id}"}

@router.get("/{gateway_id}/connections")
async def get_gateway_connections(gateway_id: int):
    return {"message": f"Connections for gateway {gateway_id}"}

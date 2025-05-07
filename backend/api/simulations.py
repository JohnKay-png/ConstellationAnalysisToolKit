from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/")
async def get_simulations():
    return {"message": "Get all simulations"}

@router.post("/")
async def create_simulation():
    return {"message": "Simulation created"}

@router.get("/{simulation_id}")
async def get_simulation(simulation_id: int):
    return {"message": f"Get simulation {simulation_id}"}

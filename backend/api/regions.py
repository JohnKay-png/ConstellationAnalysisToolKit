from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/")
async def get_regions():
    return {"message": "Get all geographic regions"}

@router.get("/{region_id}")
async def get_region(region_id: int):
    return {"message": f"Get region {region_id}"}

@router.get("/{region_id}/coverage")
async def get_region_coverage(region_id: int):
    return {"message": f"Coverage data for region {region_id}"}

from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime, timedelta
import random

router = APIRouter()

# Mock satellite data
SATELLITES = [
    {"id": 1, "name": "Satellite A"},
    {"id": 2, "name": "Satellite B"},
    {"id": 3, "name": "Satellite C"},
]

@router.get("/")
async def get_satellites():
    return SATELLITES

@router.get("/{satellite_id}")
async def get_satellite(satellite_id: int):
    satellite = next((s for s in SATELLITES if s["id"] == satellite_id), None)
    if not satellite:
        raise HTTPException(status_code=404, detail="Satellite not found")
    return satellite

@router.get("/{satellite_id}/trajectory")
async def get_satellite_trajectory(satellite_id: int, hours: int = 24):
    """Generate mock trajectory data for a satellite"""
    if hours > 168:  # Limit to 1 week
        hours = 168
    
    # Generate mock trajectory points
    now = datetime.utcnow()
    trajectory = []
    for i in range(hours):
        timestamp = now - timedelta(hours=i)
        trajectory.append({
            "timestamp": timestamp.isoformat(),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "altitude": random.uniform(100, 1000)
        })
    
    return {
        "satellite_id": satellite_id,
        "trajectory": sorted(trajectory, key=lambda x: x["timestamp"])
    }

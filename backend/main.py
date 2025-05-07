from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# 导入路由
from api import satellites, simulations, users, analysis, regions, gateways

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时加载模型和数据
    print("加载卫星数据库和计算模型...")
    yield
    # 关闭时的清理操作
    print("清理资源...")

# 创建FastAPI应用
app = FastAPI(
    title="Satellite Analysis Platform",
    description="基于卫星系统模拟与分析的平台",
    version="1.0.0",
    lifespan=lifespan
)

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载API路由
app.include_router(users.router, prefix="/api/users", tags=["用户管理"])
app.include_router(satellites.router, prefix="/api/satellites", tags=["卫星系统"])
app.include_router(simulations.router, prefix="/api/simulations", tags=["模拟管理"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["分析工具"])
app.include_router(regions.router, prefix="/api/regions", tags=["地理区域"])
app.include_router(gateways.router, prefix="/api/gateways", tags=["网关管理"])

# 挂载静态文件
app.mount("/static", StaticFiles(directory="../static"), name="static")

@app.get("/")
async def root():
    return {"message": "欢迎使用卫星分析平台API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

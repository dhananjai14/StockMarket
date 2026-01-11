# Application factory
from fastapi import FastAPI
from .blueprints.routes import router as api_router

def create_app():
    app = FastAPI(title="StockMarket-API")
    
    # Register Blueprints
    app.include_router(api_router, prefix="")
    return app
from fastapi import FastAPI

from app.database import Base, engine

# Import all models
from app.models.user import User
from app.models.audience import Audience
from app.models.campaign import Campaign
from app.models.organization import Organization
from app.routes.organization import router as organization_router
# Import all routers
from app.routes.auth import router as auth_router
from app.routes.admin import router as admin_router
from app.routes.audience import router as audience_router
from app.routes.campaign import router as campaign_router
# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-Based Multilingual Mass Communication Platform",
    version="1.0.0"
)

# Register routers
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(audience_router)
app.include_router(campaign_router)
app.include_router(organization_router)
@app.get("/")
def home():
    return {
        "message": "API is working!"
    }
from fastapi import FastAPI

from app.database import Base, engine

# ==========================
# Import Models
# ==========================
from app.models.user import User
from app.models.audience import Audience
from app.models.campaign import Campaign
from app.models.organization import Organization
from app.models.template import Template
from app.models.campaign_history import CampaignHistory

# ==========================
# Import Routers
# ==========================
from app.routes.auth import router as auth_router
from app.routes.admin import router as admin_router
from app.routes.audience import router as audience_router
from app.routes.campaign import router as campaign_router
from app.routes.organization import router as organization_router
from app.routes.template import router as template_router
from app.routes.campaign_history import router as campaign_history_router
from app.routes.dashboard import router as dashboard_router
from app.routes.translation import router as translation_router
# ==========================
# Create Database Tables
# ==========================
Base.metadata.create_all(bind=engine)

# ==========================
# FastAPI App
# ==========================
app = FastAPI(
    title="AI-Based Multilingual Mass Communication Platform",
    version="1.0.0"
)

# ==========================
# Register Routers
# ==========================
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(audience_router)
app.include_router(campaign_router)
app.include_router(organization_router)
app.include_router(template_router)
app.include_router(campaign_history_router)
app.include_router(dashboard_router)
app.include_router(translation_router)

@app.get("/")
def home():
    return {
        "message": "AI-Based Multilingual Mass Communication Platform API is Running Successfully"
    }
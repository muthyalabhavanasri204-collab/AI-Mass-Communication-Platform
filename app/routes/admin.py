from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def admin_dashboard(current_user=Depends(get_current_user)):

    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return {
        "message": f"Welcome Admin {current_user['sub']}"
    }


@router.get("/campaign")
def campaign_dashboard(current_user=Depends(get_current_user)):

    if current_user["role"] not in ["Admin", "Campaign Manager"]:
        raise HTTPException(
            status_code=403,
            detail="Campaign Manager access required"
        )

    return {
        "message": f"Welcome Campaign Manager {current_user['sub']}"
    }


@router.get("/communications")
def communications_dashboard(current_user=Depends(get_current_user)):

    if current_user["role"] not in ["Admin", "Communications Team"]:
        raise HTTPException(
            status_code=403,
            detail="Communications Team access required"
        )

    return {
        "message": f"Welcome Communications Team {current_user['sub']}"
    }
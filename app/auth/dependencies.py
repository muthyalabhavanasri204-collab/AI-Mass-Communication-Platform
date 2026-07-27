from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt_handler import verify_token

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    print("Credentials:", credentials)

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="No Authorization Header"
        )

    token = credentials.credentials
    print("Token:", token)

    payload = verify_token(token)
    print("Payload:", payload)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload


def admin_required(current_user=Depends(get_current_user)):
    print("Current User:", current_user)

    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user
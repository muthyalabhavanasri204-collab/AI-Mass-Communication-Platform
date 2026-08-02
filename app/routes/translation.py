from fastapi import APIRouter

from app.services.translation_service import translate_text

router = APIRouter(
    prefix="/translation",
    tags=["AI Translation"]
)


@router.get("/")
def translate(message: str):

    return {
        "English": message,
        "Telugu": translate_text(message, "Telugu"),
        "Hindi": translate_text(message, "Hindi"),
        "Tamil": translate_text(message, "Tamil"),
        "Kannada": translate_text(message, "Kannada"),
        "Malayalam": translate_text(message, "Malayalam")
    }
from fastapi import APIRouter

from app.domain.companions import COMPANIONS
from app.schemas.companions import CompanionOut

router = APIRouter()


@router.get("", response_model=list[CompanionOut])
def list_companions():
    return COMPANIONS

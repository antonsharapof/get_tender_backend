from fastapi import APIRouter, Depends
from db.init_db import Session, get_session
from services.auth import get_current_user
from services.tender import TenderService, get_tenders_list
from schemas.tender_schema import TenderMain
from typing import List

router = APIRouter(
    prefix="/tenders",
    tags=["tenders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list", response_model=List[TenderMain])
async def get_list(db: Session = Depends(get_session)):
    return await get_tenders_list(db)

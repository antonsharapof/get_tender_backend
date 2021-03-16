from fastapi import APIRouter, Depends
from get_tender_backend.db.init_db import Session, get_session
from get_tender_backend.services.auth import get_current_user
from get_tender_backend.services.tender import get_tenders_list
from get_tender_backend.schemas.tender_schema import TenderMain
from typing import List

router = APIRouter(
    prefix="/tenders",
    tags=["tenders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list", response_model=List[TenderMain])
async def get_list(start: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    return await get_tenders_list(db, start=start, limit=limit)




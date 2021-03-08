from fastapi import APIRouter, Depends

from services.auth import get_current_user
from services.tender import TenderService
from typing import List
from schemas import tender_schema, auth
from db import init_db


router = APIRouter(
    prefix="/tenders",
    tags=["tenders"],
    responses={404: {"description": "Not found"}},
)



@router.get("/list")
async def get_list(service: TenderService = Depends()):
    return await service.get_all_tenders()



@router.post("/filtered_list")
async def get_filtered_list(data: tender_schema.FilterParams):
     s = TenderService()
     return await s.get_filtered_tenders(data)


# @router.post("/filtered_list")
# async def get_filtered_list(data: tender_schema.FilterParams):
#     print(data)
#     return data

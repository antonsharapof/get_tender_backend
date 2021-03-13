from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class TenderAddInfo(BaseModel):
    auction_date: date
    auction_time: date

class TenderContacts(BaseModel):
    region: str = None
    customer: str = None
    mailing_address: str = None
    located: str = None
    person: str = None
    email: str = None
    phone: str = None

    class Config:
        orm_mode = True


class TenderMain(BaseModel):
    number: str = None
    type: str = None
    status: str = None
    start_price: str = None
    procurement_object: str = None
    customer: str = None
    posted: date = None
    updated: date = None
    deadline: date = None
    tender_way: str = None
    platform: str = None
    contacts: List[TenderContacts]
    add_info: List[TenderAddInfo]

    class Config:
        orm_mode = True


class FilterParams(BaseModel):
    type: Optional[List] = ["44-ФЗ\nЭлектронный аукцион", "223"]
    status: Optional[List] = ["Подача заявок", "Завершено"]

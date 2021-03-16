from sqlalchemy import desc
from get_tender_backend.db.init_db import Session
from get_tender_backend.models.tender_models import TenderMain as TM


async def get_tenders_list(db: Session, start: int = 0, limit: int = 20):
    if start == 0:
        tenders = db.query(TM).order_by(desc(TM.id)).offset(0).limit(limit).all()
    else:
        tenders = db.query(TM).filter(TM.id < start).order_by(desc(TM.id)).offset(0).limit(limit).all()
    return tenders


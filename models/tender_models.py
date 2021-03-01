from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.init_db import Base


class TenderInfo(Base):
    __tablename__ = 'tender_info'

    tender_number = Column(String, primary_key=True)
    tender_stage = Column(String)
    tender_market = Column(String)
    doc = relationship("TenderDocs", backref="tender")


class TenderDocs(Base):
    __tablename__ = 'tender_documents'

    tender_number = Column(String, ForeignKey(TenderInfo.tender_number))
    document_name = Column(String)
    document_link = Column(String, primary_key=True)
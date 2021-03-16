from sqlalchemy import Column, Integer, String, ForeignKey, Date, INTEGER
from sqlalchemy.orm import relationship

from get_tender_backend.db.init_db import Base


class TenderMain(Base):

    __tablename__ = 'tender_main'

    id = Column(Integer, autoincrement=True, primary_key=True)
    number = Column(String)
    type = Column(String)
    status = Column(String)
    start_price = Column(String)
    procurement_object = Column(String)
    customer = Column(String)
    posted = Column(Date)
    updated = Column(Date)
    deadline = Column(Date)
    tender_way = Column(String)
    platform = Column(String)

    contacts = relationship("TenderContactInfo", backref="tender_main")
    add_info = relationship("TenderAddInfo", backref="tender_main")

class TenderAddInfo(Base):

    __tablename__ = 'tender_add_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tender_number = Column(String, ForeignKey('tender_main.number'))
    auction_date = Column(Date)
    auction_time = Column(Date)





class TenderContactInfo(Base):

    __tablename__ = 'tender_contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tender_number = Column(String, ForeignKey('tender_main.number'))
    region = Column(String)
    customer = Column(String)
    mailing_address = Column(String)
    located = Column(String)
    person = Column(String)
    email = Column(String)
    phone = Column(String)




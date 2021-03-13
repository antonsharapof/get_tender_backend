from db.init_db import mongo_db, get_session
from models.tender_models import TenderMain as TM, TenderContactInfo as TC




class TenderService:
    def __init__(self):
        pass

    # async def __make_tender_list(self, cursor):
    #     all_tenders = []
    #     for document in await cursor.to_list(length=100):
    #         document.pop('_id')
    #         all_tenders.append(document)
    #     return all_tenders
    #
    # async def get_all_tenders(self):
    #     cursor = mongo_db.test_collection.find()
    #     return await self.__make_tender_list(cursor)
    #
    # async def get_filtered_tenders(self, params: tender_schema.FilterParams):
    #     cursor = mongo_db.test_collection.find({"type_tender": {'$in': params.type},
    #                                             "tender_status": {'$in': params.status}})
    #     return await self.__make_tender_list(cursor)


async def get_tenders_list(db):
    tenders = db.query(TM).all()
    return tenders


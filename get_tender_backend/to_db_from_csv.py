from get_tender_backend.db.init_db import Session
from get_tender_backend.models import tender_models
import pandas as pd


def main():
    db = Session()
    df = pd.read_csv('test_collection.csv')
    # df['Дата проведения аукциона ']
    # df['Время проведения аукциона'] =
    for index, row in df.iterrows():
        tender = tender_models.TenderMain(
            number=row['tender_number'],
            type=row['type_tender'],
            status=row['tender_status'],
            start_price=row['start_price'],
            procurement_object=row['Объект закупки'],
            customer=row['Заказчик'],
            posted=pd.to_datetime(row['Размещено'], errors='ignore'),
            updated=pd.to_datetime(row['Обновлено'], errors='ignore'),
            deadline=pd.to_datetime(row['Окончание подачи заявок'], errors='ignore'),
            tender_way=row['Способ определения постав'],
            platform=row['Наименование электронной ']
        )
        tender_contacts = tender_models.TenderContactInfo(
            tender_number = ['tender_number'],
            region=row['Регион'],
            customer=row['Заказчик'],
            mailing_address=row['Почтовый адрес'],
            located=row['Место нахождения'],
            person=row['Ответственное должностное'],
            email=row['Адрес электронной почты'],
            phone=row['Номер контактного телефон']
        )
        print(type(row['Дата проведения аукциона ']))
        tender_add_info = tender_models.TenderAddInfo(
            tender_number = row['tender_number'],
            auction_date = pd.to_datetime(row['Дата проведения аукциона '] if type(row['Дата проведения аукциона ']) == str else '01.01.2001', errors='raise'),
            auction_time = pd.to_datetime(row['Время проведения аукциона'] if type(row['Время проведения аукциона']) == str else '01.01.2001', errors='raise')
        )
        tender.contacts.append(tender_contacts)
        db.add(tender)
        db.add(tender_contacts)
        db.add(tender_add_info)
        db.commit()


if __name__ == "__main__":
    main()

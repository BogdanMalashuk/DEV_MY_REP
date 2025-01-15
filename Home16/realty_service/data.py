from classes import *
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///myDatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


user1 = User(name='Bogdan', email='bogdan@mail.ru')
user2 = User(name='Sergei', email='sergei@mail.ru')
user3 = User(name='Eduard', email='eduard@mail.ru')
session.add_all([user1, user2, user3])

property1 = Property(address='p1-street 12', is_commercial=True, rent_price=2300)
property2 = Property(address='p2-street 9', is_commercial=False, rent_price=600)
property3 = Property(address='p3-street 55', is_commercial=False, rent_price=7000)
property4 = Property(address='p4-street 101', is_commercial=True, rent_price=920)
session.add_all([property1, property2, property3, property4])
session.commit()

sd_l1 = date(2024, 12, 3)
sd_l2 = date(2022, 9, 28)
sd_l3 = date(2025, 4, 11)
sd_l4 = date(2022, 2, 16)
sd_l5 = date(2025, 8, 15)

ed_l1 = date(2025, 7, 3)
ed_l2 = date(2026, 5, 28)
ed_l3 = date(2027, 5, 11)
ed_l4 = date(2025, 12, 16)
ed_l5 = date(2030, 4, 25)

lease1 = Lease(start_date=sd_l1, end_date=ed_l1, user_id=user1.id, property_id=property1.id)
lease2 = Lease(start_date=sd_l2, end_date=ed_l2, user_id=user2.id, property_id=property4.id)
lease3 = Lease(start_date=sd_l3, end_date=ed_l3, user_id=user1.id, property_id=property3.id)
lease4 = Lease(start_date=sd_l4, end_date=ed_l4, user_id=user3.id, property_id=property2.id)
lease5 = Lease(start_date=sd_l5, end_date=ed_l5, user_id=user3.id, property_id=property4.id)
session.add_all([lease1, lease2, lease3, lease4, lease5])
session.commit()

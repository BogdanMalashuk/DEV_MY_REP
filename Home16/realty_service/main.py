import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from classes import *


engine = create_engine('sqlite:///myDatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def make_payment(lease_id):
    lease = session.query(Lease).filter_by(id=lease_id).first()
    amount = int(input('enter amount summ: '))
    payment = Payment(amount=amount, payment_date=datetime.date.today(), lease_id=lease.id)
    session.add(payment)

    lease.already_summ += amount
    if lease.already_summ > 0 and not lease.is_active:
        lease.is_active = True
    session.commit()


def complete_lease(lease_id):
    lease = session.query(Lease).filter_by(id=lease_id).first()
    if lease.is_active:
        lease.is_active = False
        session.commit()
        return 'lease successfully completed!'
    else:
        return 'lease is already completed'


def debtors():
    users_with_payments = session.query(Payment.lease_id).distinct()
    users = session.query(User).join(Lease).filter(~Lease.id.in_(users_with_payments)).all()
    return users


def popular_properties():
    properties = (
        session.query(Property)
        .join(Lease)
        .group_by(Property.id)
        .having(func.count(Lease.id) > 3)
        .all()
    )
    return properties


def atomar_operation(user_id, property_id, start_date, end_date, payment_amount):
    try:
        lease = Lease(user_id=user_id, property_id=property_id, start_date=datetime.date.today(), end_date=end_date)
        session.add(lease)
        session.flush()
        payment = Payment(amount=payment_amount, payment_date=start_date, lease_id=lease.id)
        session.add(payment)
        lease.already_summ += payment_amount
        lease.is_active = True
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def agent_comm(agent_id):
    agent = session.query(Agent).filter_by(id=agent_id).first()
    if not agent:
        return 'agent not found'
    leases = session.query(Lease).filter_by(agent_id=agent.id).all()
    commission = sum(lease.property.rent_price * agent.commission for lease in leases)
    return commission

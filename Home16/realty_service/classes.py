from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String)

    leases = relationship('Lease', back_populates='user', cascade='all, delete')


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, nullable=False)
    is_commercial = Column(Boolean)
    rent_price = Column(Float, nullable=False)

    leases = relationship('Lease', back_populates='property', cascade='all, delete')


class Lease(Base):
    __tablename__ = 'leases'
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date)
    end_date = Column(Date)
    already_summ = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    is_active = Column(Boolean, default=True)
    agent_id = Column(Integer, ForeignKey('agents.id'))

    property = relationship('Property', back_populates='leases')
    user = relationship('User', back_populates='leases')
    payment = relationship('Payment', back_populates='lease')
    agent = relationship('Agent', back_populates='leases')

    def __str__(self):
        return f'lease id: {self.id}'


class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date)
    lease_id = Column(Integer, ForeignKey('leases.id'))

    lease = relationship('Lease', back_populates='payment')


class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    commission = Column(Float, default=0.05)

    leases = relationship('Lease', back_populates='agent')

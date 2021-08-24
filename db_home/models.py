from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column, String,
    Integer, DateTime,
    Boolean, ForeignKey,
)
from sqlalchemy.orm import relationship

db = SQLAlchemy()
Base = db.Model


class Status:
    WAITING = 'WAITING'
    PROCESSING = 'PROCESSING'
    EXECUTED = 'EXECUTED'
    REJECTED = 'REJECTED'
    CANCELLED = 'CANCELLED'
    EXCEED = 'EXCEED'


class Manager(Base):
    __tablename__ = 't_manager'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=True)
    surname = Column(String(256), default='')
    name = Column(String(256), default='')
    last_name = Column(String(256), default='')
    branch = Column(String(64), default='')
    date_create = Column(DateTime, default=datetime.now())
    blocked = Column(Boolean, default=False)

    def __repr__(self):
        return f'{self.name}'


class Client(Base):
    __tablename__ = 't_client'

    id = Column(Integer, primary_key=True, unique=True)
    surname = Column(String(256), default='')
    name = Column(String(256), default='')
    last_name = Column(String(256), default='')
    inn = Column(String(255), nullable=True)
    email = Column(String(256))
    client_info = Column(String(256))
    payment_account = Column(String(64))
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return f'{self.name}'


class Order(Base):
    __tablename__ = 't_order'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.id))
    status = Column(String(32))
    err_code = Column(Integer)
    err_message = Column(String(500))
    client_code = Column(String(64))
    branch_code = Column(String(64))
    manager_created_id = Column(Integer, ForeignKey(Manager.id))
    manager_confirm_id = Column(Integer, ForeignKey(Manager.id))
    date_create = Column(DateTime)
    date_confirm = Column(DateTime)

    client = relationship(Client)
    manager_created = relationship(
        Manager, foreign_keys='Order.manager_created_id',
    )
    manager_confirm = relationship(
        Manager, foreign_keys='Order.manager_confirm_id',
    )


class OrderHistory(Base):
    __tablename__ = 't_order_history'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.id))
    manager_id = Column(Integer, ForeignKey(Manager.id))
    new_status = Column(String(32))
    note_of_change = Column(String(500))
    date = Column(DateTime)
    err_code = Column(Integer)
    err_message = Column(String(500))

    manager = relationship(Manager)

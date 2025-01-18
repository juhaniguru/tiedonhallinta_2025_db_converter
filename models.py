from sqlalchemy import Column, MetaData, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm.base import Mapped

metadata = MetaData()


t_users_denormalized = Table(
    'users_denormalized', metadata,
    Column('name', String(255), nullable=False),
    Column('address', String(255), nullable=False),
    Column('phone_numbers', String(255))
)


t_users_nf1 = Table(
    'users_nf1', metadata,
    Column('id', INTEGER(11), nullable=False),
    Column('first_name', String(45), nullable=False),
    Column('last_name', String(45), nullable=False),
    Column('street', String(45), nullable=False),
    Column('zip_code', String(45), nullable=False),
    Column('city', String(45), nullable=False),
    Column('phone_number', String(45))
)

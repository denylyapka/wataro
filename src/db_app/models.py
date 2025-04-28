from typing import List

from sqlalchemy import BigInteger, Date, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class TgData(Base):
    __tablename__ = "tg_data"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    username = Column(String)
    fullname = Column(String)

class AccountMetricsData(Base):
    __tablename__ = "account_metrics_data"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    username = Column(String, nullable=True)
    name = Column(String, nullable=True)
    paul = Column(String, nullable=True)
    device = Column(String, nullable=True)


class CardDeal(Base):
    __tablename__ = "card_deal"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    question = Column(String, nullable=False)
    card_deal = Column(String, nullable=False)


class RequestHistory(Base):
    __tablename__ = "request_history"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    question = Column(String, nullable=False)


class SubsCheckUser_2(Base):
    __tablename__ = "subs_check_user_2"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, nullable=False)
    flag = Column(String, nullable=False)


class ReferalShip(Base):
    __tablename__ = "referal_ship"

    id = Column(Integer, primary_key=True)
    tg_id_master = Column(BigInteger, nullable=False)
    tg_id_friend = Column(BigInteger, nullable=False)
    code = Column(String, nullable=False)

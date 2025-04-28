from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@127.0.0.1:5432/db_taro_test'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/db_taro_test'
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

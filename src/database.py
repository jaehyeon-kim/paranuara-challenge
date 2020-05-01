import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

os.environ["POSTGRES_USER"] = "devuser"
os.environ["POSTGRES_PASSWORD"] = "password"
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_DB"] = "devdb"

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:5432/{}".format(
    os.environ["POSTGRES_USER"],
    os.environ["POSTGRES_PASSWORD"],
    os.environ["POSTGRES_HOST"],
    os.environ["POSTGRES_DB"],
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

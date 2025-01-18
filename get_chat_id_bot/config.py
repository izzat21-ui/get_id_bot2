import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:0@localhost:5432/postgres")

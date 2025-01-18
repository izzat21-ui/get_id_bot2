from typing import List, Optional
from sqlalchemy import ForeignKey, BIGINT, Date, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from config import engine


# Base model
class Base(DeclarativeBase):
    pass


# User model
class User(Base):
    __tablename__ = "users"

    # chat_id primary key
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)

    # Optional user details
    first_name: Mapped[Optional[str]] = mapped_column(String, nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    username: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)

    # birth_day (nullable, unique, Date)
    birth_day: Mapped[Optional[Date]] = mapped_column(Date, unique=True, nullable=True)


# Create all tables
Base.metadata.create_all(engine)

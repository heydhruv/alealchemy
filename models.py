import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Timings(Base):
    __abstract__ = True
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)


class User(Timings):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(15), unique=True, nullable=False)
    email = sa.Column(sa.String(120), unique=True, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)




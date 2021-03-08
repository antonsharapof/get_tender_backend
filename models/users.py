from db.init_db import Base
import sqlalchemy as sa

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text)
    username = sa.Column(sa.Text, unique=True)
    position = sa.Column(sa.Text)
    password_hash = sa.Column(sa.Text)
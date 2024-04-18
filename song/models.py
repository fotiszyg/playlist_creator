from sqlalchemy import (
    Column,
    String
)
from sqlalchemy.types import Integer

from database.extensions import db, Base


class Song(db.Model):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    artist = Column(String(128))
    album = Column(String(128))
    year = Column(Integer)

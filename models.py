from app import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Catalog(db.Model):
    __tableName__ = "Catalog"

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True)
    title = Column(db.String(128), nullable=False)
    description = Column(db.Text)
    entrypoint = Column(db.String(256), nullable=False)
    state = Column(db.Integer, default=1)

    __table_args__ = {'schema': 'public'}

    def __repr__(self):
        return f'{self.id}: {self.title} /{self.entrypoint} status={self.state}'

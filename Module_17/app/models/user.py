from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    task = relationship('Task', back_populates='users')


from sqlalchemy.schema import CreateTable


print(CreateTable(User.__table__))

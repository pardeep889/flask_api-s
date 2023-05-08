import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()



engine = db.create_engine("mysql+mysqlconnector://root:@localhost:3306/sqlalchemy")

connection = engine.connect()

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

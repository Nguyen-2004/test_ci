from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if not session.query(User).first():
    session.add_all([
        User(name="Nguyễn Văn A", email="a@example.com"),
        User(name="Trần Thị B", email="b@example.com"),
        User(name="Lê Văn C", email="c@example.com"),
    ])
    session.commit()

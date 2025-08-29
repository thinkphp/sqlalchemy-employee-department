from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Conectare la MySQL
engine = create_engine("mysql+mysqlconnector://snake:adidas88_AS@localhost/BalabacDB")

Base = declarative_base()

# Definirea modelului ORM
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)

# Crearea tabelului în baza de date
Base.metadata.create_all(engine)

# Crearea unei sesiuni
Session = sessionmaker(bind=engine)
session = Session()

# Adăugarea unui utilizator
new_user = User(name="Adrian", email="adrian@gmail.com", age=28)
session.add(new_user)
session.commit()

# Interogare
users = session.query(User).all()
for user in users:
    print(user.name, user.email)

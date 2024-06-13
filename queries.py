from sqlalchemy.orm import sessionmaker

from database import engine
from models import User

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

user1 = User(username='user1', email='user1@gmail.com')
user2 = User(username='user2', email='user2@gmail.com')
user3 = User(username='user3', email='user3@gmail.com')
user4 = User(username='user4', email='user4@gmail.com')


db.add_all([user1, user2, user3, user4])

db.commit()

db.close()

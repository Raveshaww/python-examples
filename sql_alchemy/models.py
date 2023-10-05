from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Creates the base class, which all models need to inherit from for Alembic to map
# tables / columns in our database
Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # basically creates a more readable representation of the object
    # useful for when we want to print the object
    def __repr__(self):
        return (
            f'UserModel(id={self.id}, first_name={self.first_name}',
            f'last_name={self.last_name}, birth={self.birth}',
            f'created={self.created})'
        )


# List of users to add to database
users = [
    UserModel(first_name='Rave', last_name='Ravenmore', birth=datetime(1994, 9, 21)),
    UserModel(first_name='Fid', last_name='Ravenmore', birth=datetime(1990, 1, 29)),
]

# We need to connect to the database, so we create a sessionmaker
session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

# Create the users 
def create_users():
    # Create a new session everytime you want to interact with a database
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

# create_users()

# Query info
with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)
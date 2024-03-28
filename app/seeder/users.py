import bcrypt
from app.models import db, User
from sqlalchemy import text

def seed_users():
    demo_user1 = User(
        firstName = 'John',
        lastName = 'Doe',
        email = 'johndoe@gmail.com',
        hashedPassword = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()),
        loginMethod = 'traditional'
    )

    demo_user2 = User(
        firstName ='Mary',
        lastName = 'Smith',
        email = 'marys@gmail.com',
        hashedPassword = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()),
        loginMethod = 'traditional'
    )

    demo_user3 = User(
        firstName ='Sarah',
        lastName = 'Brown',
        email = 'sarahb@gmail.com',
        hashedPassword = bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()),
        loginMethod = 'traditional'
    )

    db.session.add(demo_user1)
    db.session.add(demo_user2)
    db.session.add(demo_user3)

    db.session.commit()

def undo_users():
    db.session.execute(text('TRUNCATE users RESTART IDENTITY CASCADE;'))
    db.session.commit()

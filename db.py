from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session

engine = create_engine("postgresql+psycopg2://postgres:city@localhost/login")
session = create_session(bind=engine)

def login(name, psw):
    a = session.execute(text(f"SELECT * FROM users WHERE login='{name}' AND password='{psw}'")).fetchall()
    session.commit()
    session.close()
    if a:
        return a
    else:
        return False
from sqlmodel import create_engine, Session

DATABASE_URL = "postgresql://livros_user:123456@localhost:5432/livros_db"

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
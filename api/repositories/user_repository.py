from sqlmodel import Session, select

from api.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def criar_usuario(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def buscar_por_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
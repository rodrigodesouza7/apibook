from sqlmodel import Session, select
from uuid import UUID

from api.models import Livro


class LivroRepository:
    def __init__(self, session: Session):
        self.session = session

    def listar(self, user_id: UUID, offset: int, limit: int):
        statement = (
            select(Livro)
            .where(Livro.user_id == user_id)
            .offset(offset)
            .limit(limit)
        )
        return self.session.exec(statement).all()

    def obter(self, livro_id: UUID, user_id: UUID):
        statement = select(Livro).where(
            Livro.uuid == livro_id,
            Livro.user_id == user_id
        )
        return self.session.exec(statement).first()

    def criar(self, livro: Livro):
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def atualizar(self, livro: Livro):
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def deletar(self, livro: Livro):
        self.session.delete(livro)
        self.session.commit()
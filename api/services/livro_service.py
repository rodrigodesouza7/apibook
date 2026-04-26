from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session

from api.models import (
    Livro,
    LivroPost,
    LivroPut,
    LivroPatch,
    LivroResposta,
    ConfirmaDelete,
)
from api.repositories.livro_repository import LivroRepository


class LivroService:
    def __init__(self, session: Session):
        self.repository = LivroRepository(session)

    def listar(self, user_id: UUID, offset: int, limit: int):
        livros = self.repository.listar(user_id, offset, limit)
        return [LivroResposta.model_validate(l) for l in livros]

    def obter(self, livro_id: UUID, user_id: UUID):
        livro = self.repository.obter(livro_id, user_id)
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        return LivroResposta.model_validate(livro)

    def criar(self, livro_data: LivroPost, user_id: UUID):
        livro = Livro(
            **livro_data.model_dump(),
            user_id=user_id
        )
        livro = self.repository.criar(livro)
        return LivroResposta.model_validate(livro)

    def atualizar(self, livro_id: UUID, livro_data: LivroPut, user_id: UUID):
        livro = self.repository.obter(livro_id, user_id)
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")

        for key, value in livro_data.model_dump().items():
            setattr(livro, key, value)

        livro = self.repository.atualizar(livro)
        return LivroResposta.model_validate(livro)

    def atualizar_parcial(self, livro_id: UUID, livro_data: LivroPatch, user_id: UUID):
        livro = self.repository.obter(livro_id, user_id)
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")

        update_data = livro_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(livro, key, value)

        livro = self.repository.atualizar(livro)
        return LivroResposta.model_validate(livro)

    def deletar(self, livro_id: UUID, user_id: UUID):
        livro = self.repository.obter(livro_id, user_id)
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")

        self.repository.deletar(livro)
        return ConfirmaDelete(
            mensagem="Livro deletado",
            uuid=livro_id
        )
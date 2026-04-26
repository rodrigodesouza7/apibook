from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Annotated
from uuid import UUID

from api.database import get_session
from api.models import (
    LivroPost,
    LivroPut,
    LivroPatch,
    LivroResposta,
    ConfirmaDelete,
)
from api.services.livro_service import LivroService
from api.core.deps import get_current_user

router = APIRouter(prefix="/livros", tags=["livros"])

SessionDep = Annotated[Session, Depends(get_session)]


def get_service(session: SessionDep) -> LivroService:
    return LivroService(session)


@router.get("/", response_model=list[LivroResposta])
def listar_livros(
    offset: int = 0,
    limit: int = 10,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.listar(UUID(user_id), offset, limit)


@router.get("/{livro_id}", response_model=LivroResposta)
def obter_livro(
    livro_id: UUID,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.obter(livro_id, UUID(user_id))


@router.post("/", response_model=LivroResposta)
def criar_livro(
    livro: LivroPost,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.criar(livro, UUID(user_id))


@router.put("/{livro_id}", response_model=LivroResposta)
def atualizar_livro(
    livro_id: UUID,
    livro: LivroPut,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.atualizar(livro_id, livro, UUID(user_id))


@router.patch("/{livro_id}", response_model=LivroResposta)
def atualizar_parcial(
    livro_id: UUID,
    livro: LivroPatch,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.atualizar_parcial(livro_id, livro, UUID(user_id))


@router.delete("/{livro_id}", response_model=ConfirmaDelete)
def deletar_livro(
    livro_id: UUID,
    service: LivroService = Depends(get_service),
    user_id: str = Depends(get_current_user),
):
    return service.deletar(livro_id, UUID(user_id))
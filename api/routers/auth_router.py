from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Annotated

from api.database import get_session
from api.models import UserCreate, UserLogin, UserResposta
from api.services.user_service import UserService
from api.core.auth import criar_token

router = APIRouter(prefix="/auth", tags=["auth"])

SessionDep = Annotated[Session, Depends(get_session)]


def get_service(session: SessionDep) -> UserService:
    return UserService(session)


# 📌 REGISTER
@router.post("/register", response_model=UserResposta)
def register(
    user: UserCreate,
    service: UserService = Depends(get_service),
):
    return service.criar_usuario(user)


# 📌 LOGIN COM JWT
@router.post("/login")
def login(
    user: UserLogin,
    service: UserService = Depends(get_service),
):
    usuario = service.autenticar_usuario(user.email, user.senha)

    token = criar_token({"sub": str(usuario.uuid)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
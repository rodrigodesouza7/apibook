from fastapi import HTTPException
from sqlmodel import Session

from api.models import User, UserCreate, UserResposta
from api.repositories.user_repository import UserRepository
from api.core.security import hash_senha, verificar_senha


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def criar_usuario(self, user_data: UserCreate) -> UserResposta:
        # Verifica se email já existe
        if self.repository.buscar_por_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado")

        # Gera hash da senha
        senha_hash = hash_senha(user_data.senha)

        # Cria usuário
        user = User(
            email=user_data.email,
            senha_hash=senha_hash
        )

        user = self.repository.criar_usuario(user)

        return UserResposta(
            uuid=user.uuid,
            email=user.email
        )

    def autenticar_usuario(self, email: str, senha: str) -> User:
        user = self.repository.buscar_por_email(email)

        if not user:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        if not verificar_senha(senha, user.senha_hash):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        return user
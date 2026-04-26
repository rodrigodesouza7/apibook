from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.routers.livros_router import router as livro_router
from api.routers.auth_router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔹 Aqui você pode colocar inicializações futuras
    yield
    # 🔹 Aqui pode fechar conexões, etc.


def create_app() -> FastAPI:
    app = FastAPI(
        title="BookFlow API",
        version="1.0.0",
        lifespan=lifespan
    )

    # 📚 Rotas de livros
    app.include_router(livro_router)

    # 🔐 Rotas de autenticação
    app.include_router(auth_router)

    return app


app = create_app()
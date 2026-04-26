📚 API Book — Gestão de Livros com FastAPI

API backend para gerenciamento de livros com autenticação de usuários, permitindo operações completas de CRUD com isolamento de dados por usuário.

🎯 Objetivo

Fornecer uma API robusta e segura para:

Gerenciar livros por usuário
Garantir isolamento de dados (multi-user)
Aplicar boas práticas de arquitetura backend
Servir como base para aplicações reais e portfólio profissional
🧠 Problema

APIs simples de CRUD geralmente não resolvem:

Controle de acesso por usuário
Isolamento de dados
Estrutura escalável
Segurança básica (autenticação)

Este projeto resolve:

✔ Separação de dados por usuário (multi-user)
✔ Autenticação segura com JWT
✔ Estrutura modular e escalável
✔ Consistência entre aplicação e banco
💼 Aplicações no Mundo Real
📚 Sistemas de bibliotecas
📖 Apps de leitura pessoal
🧾 Sistemas de catálogo
🧠 Bases para SaaS multi-tenant
🔐 APIs com controle de acesso por usuário
🏗️ Arquitetura do Sistema

O sistema segue uma arquitetura em camadas:

Router (FastAPI)
↓
Service (regras de negócio)
↓
Repository (acesso ao banco)
↓
Database (PostgreSQL)

Com autenticação integrada:

JWT → Depends → Proteção de rotas
🛠️ Tecnologias Utilizadas
Python
FastAPI
SQLModel
PostgreSQL
Alembic
Pydantic
Passlib (hash de senha)
Python-Jose (JWT)
Pytest
📁 Estrutura do Projeto
apibook/
├── api/
│ ├── routers/
│ │ ├── livros_router.py
│ │ └── auth_router.py
│ ├── services/
│ │ └── livro_service.py
│ ├── repositories/
│ │ └── livro_repository.py
│ ├── core/
│ │ ├── auth.py
│ │ └── deps.py
│ ├── models.py
│ ├── database.py
│ └── main.py
│
├── tests/
│ ├── test_auth.py
│ └── test_livros.py
│
├── alembic/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
▶️ Como Executar o Projeto

1. Clonar o repositório
   git clone https://github.com/rodrigodesouza7/apibook.git
   cd apibook
2. Criar ambiente virtual
   python -m venv venv
   source venv/bin/activate
3. Instalar dependências
   pip install -r requirements.txt
4. Configurar variáveis de ambiente

Crie um arquivo .env:

DATABASE_URL=postgresql://usuario:senha@localhost/livros_db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256 5. Rodar migrações
alembic upgrade head 6. Rodar aplicação
uvicorn api.main:app --reload 7. Acessar documentação
http://127.0.0.1:8000/docs
🔐 Autenticação

Fluxo:

POST /auth/register
POST /auth/login → retorna JWT

Uso:

Authorization: Bearer SEU_TOKEN
📚 Endpoints Principais
GET /livros/
POST /livros/
GET /livros/{id}
PUT /livros/{id}
PATCH /livros/{id}
DELETE /livros/{id}
🧪 Testes

Executar:

pytest -v
✅ Cobertura de Testes
✔ Registro e login
✔ Criação de livros
✔ Listagem de livros
✔ Isolamento entre usuários (multi-user)
✔ Fluxo completo autenticado
🚀 Diferenciais do Projeto
✔ Autenticação JWT completa
✔ Multi-user com isolamento de dados
✔ Arquitetura em camadas
✔ Migrations com Alembic
✔ Testes automatizados reais
✔ Validação end-to-end (curl + pytest)
✔ Código modular e escalável
🔮 Possíveis Evoluções

- Refresh token
- Sistema de roles (admin/user)
- Deploy em cloud (Render / Railway)
- Logging estruturado
- Paginação avançada
- Cache (Redis)
  🏁 Conclusão

Este projeto demonstra:

✔ Desenvolvimento de API profissional com FastAPI
✔ Implementação de autenticação segura
✔ Estruturação em arquitetura escalável
✔ Integração com banco de dados relacional
✔ Testes automatizados e validação completa
✔ Resolução de problemas reais (migrations)


👤 Sobre o Autor

Rodrigo de Souza Silva
Profissional de Tecnologia da Informação com formação em Sistemas de Informação e pós-graduação em Data Science, Machine Learning e IA.

🔗 LinkedIn: https://www.linkedin.com/in/rodrigodesouzasilva
💻 GitHub: https://github.com/rodrigodesouza7
📄 Licença

Este projeto está licenciado sob os termos da licença MIT.

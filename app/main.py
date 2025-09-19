from .database import engine, Base
from . import controller

# cria tabelas
Base.metadata.create_all(bind=engine)

# expõe a instância FastAPI para o uvicorn: "app.main:app"
app = controller.app

Livros API

API REST simples para cadastrar, editar, remover e listar livros.
Cada livro tem: title (título), authors (autor(es)), pages (quantidade de páginas) e year (ano de publicação). Dados persistidos em SQLite.

Requisitos: Python 3.10+, pip

Comandos para setup:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

A aplicação ficará disponível em http://127.0.0.1:8000/ e para acessar a documentação:
http://127.0.0.1:8000/docs (Swagger)


Endpoints (URLs) 
Todos os endpoints usam JSON e seguem REST padrão:

GET /books
Lista todos os livros. Suporta query params ?skip=0&limit=100.

Exemplo: curl http://127.0.0.1:8000/books

GET /books/{id}
Retorna o livro com id informado.

Exemplo: curl http://127.0.0.1:8000/books/1

POST /books
Cria um novo livro. Body JSON:
{
  "title": "Título do Livro",
  "authors": "Autor A, Autor B",
  "pages": 123,
  "year": 2025
}

authors é armazenado como string (ex.: "Autor A, Autor B") para manter simplicidade.

Exemplo:
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Livro X","authors":"A,B","pages":100,"year":2025}'


PUT /books/{id} ou PATCH /books/{id} (conforme implementação)

Atualiza um livro. Para atualização parcial envie apenas os campos que quer alterar (ex.: {"title":"TesteAtualizado"}).
Strings vazias são rejeitadas por validação.

Exemplo (parcial):

curl -X PATCH http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Novo Título"}'


DELETE /books/{id}

Remove o livro com id informado.

Exemplo: curl -X DELETE http://127.0.0.1:8000/books/1

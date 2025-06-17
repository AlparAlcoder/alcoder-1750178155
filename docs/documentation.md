# Documentação da API FastAPI

Essa API é construída usando o FastAPI e é projetada para gerenciar tarefas. Ela suporta operações CRUD básicas em tarefas - criar, ler, atualizar e deletar.

## Dependências

- FastAPI: Um moderno framework web rápido (alta performance) para construção de APIs com Python 3.6+ baseado nos padrões para APIs, tais como: OpenAPI (anteriormente conhecido como Swagger) e JSON Schema.
- Pydantic: Biblioteca de análise de dados para Python com suporte para anotações de tipo padrão.

## Modelos

### Task

Modelo de tarefa que contém as seguintes propriedades:

- `id` (int): O identificador único da tarefa
- `title` (str): O título da tarefa
- `description` (str): Descrição detalhada da tarefa
- `done` (bool): Indica se a tarefa foi concluída

## Endpoints

### GET /tasks

Retorna uma lista de todas as tarefas.

**Exemplo de uso:**

```http
GET /tasks
```

### GET /tasks/{task_id}

Retorna a tarefa com o id fornecido.

**Parâmetros:**

- `task_id` (int): O identificador único da tarefa

**Exemplo de uso:**

```http
GET /tasks/1
```

### POST /tasks

Cria uma nova tarefa.

**Parâmetros:**

- `task` (Task): A tarefa para ser criada

**Exemplo de uso:**

```http
POST /tasks
Content-Type: application/json

{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Cheese, Pizza, Fruit, Tylenol", 
    "done": false
}
```

### PUT /tasks/{task_id}

Atualiza a tarefa com o id fornecido.

**Parâmetros:**

- `task_id` (int): O identificador único da tarefa
- `task` (Task): A tarefa atualizada

**Exemplo de uso:**

```http
PUT /tasks/1
Content-Type: application/json

{
    "id": 1,
    "title": "Buy groceries",
    "description": "Just milk and cheese", 
    "done": true
}
```

### DELETE /tasks/{task_id}

Deleta a tarefa com o id fornecido.

**Parâmetros:**

- `task_id` (int): O identificador único da tarefa

**Exemplo de uso:**

```http
DELETE /tasks/1
```

## Notas Importantes

- A API não possui autenticação, portanto não é recomendada para produção.
- A API não possui persistência de dados, todas as tarefas são armazenadas em memória e são perdidas quando a aplicação é encerrada.
# API de Tareas — FastAPI

API REST simple para gestionar una lista de tareas (to-do list), construida con FastAPI como proyecto de aprendizaje backend.

## Funcionalidades

- Crear tareas
- Listar tareas
- Actualizar tareas (marcar como completadas, editar título)
- Borrar tareas

## Tecnologías

- Python
- FastAPI
- Uvicorn

## Cómo correrlo localmente

\`\`\`bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
\`\`\`

Después abrí `http://127.0.0.1:8000/docs` para probar los endpoints desde la documentación interactiva.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje de bienvenida |
| POST | `/tareas` | Crear una tarea |
| GET | `/tareas` | Listar todas las tareas |
| PUT | `/tareas/{id}` | Actualizar una tarea |
| DELETE | `/tareas/{id}` | Borrar una tarea |

## Próximos pasos

- Persistencia con base de datos (SQLite)
- Autenticación de usuarios
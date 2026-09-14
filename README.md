# API de Tareas — FastAPI + SQLAlchemy

API REST para gestionar una lista de tareas (to-do list), construida con FastAPI y persistencia en base de datos SQLite, como proyecto de aprendizaje backend.

## Funcionalidades

- Crear tareas
- Listar tareas
- Actualizar tareas (marcar como completadas, editar título)
- Borrar tareas
- Persistencia real en base de datos (los datos no se pierden al reiniciar el servidor)

## Tecnologías

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Uvicorn

## Cómo correrlo localmente

\`\`\`bash
pip install fastapi uvicorn sqlalchemy
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

## Estructura del proyecto

\`\`\`
main.py       → endpoints de la API
models.py     → modelo de base de datos (SQLAlchemy)
database.py   → configuración de la conexión a la base de datos
\`\`\`

## Próximos pasos

- Autenticación de usuarios (login/registro con JWT)
- Que cada usuario vea solo sus propias tareas
- Deploy en un servidor real
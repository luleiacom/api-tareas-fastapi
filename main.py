from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TareaCrear(BaseModel):
    titulo: str
    completada: bool = False

class Tarea(BaseModel):
    id: int
    titulo: str
    completada: bool = False

tareas = []
contador_id = 0

@app.get("/")
def home():
    return {"mensaje": "API de tareas funcionando"}

@app.post("/tareas")
def crear_tarea(datos: TareaCrear):
    global contador_id
    contador_id += 1
    nueva_tarea = Tarea(id=contador_id, titulo=datos.titulo, completada=datos.completada)
    tareas.append(nueva_tarea)
    return nueva_tarea

@app.get("/tareas")
def listar_tareas():
    return tareas

@app.put("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: int, datos: TareaCrear):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tarea.titulo = datos.titulo
            tarea.completada = datos.completada
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tareas.remove(tarea)
            return {"mensaje": f"Tarea {tarea_id} borrada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
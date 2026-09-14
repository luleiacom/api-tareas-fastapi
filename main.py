from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TareaCrear(BaseModel):
    titulo: str
    completada: bool = False

class Tarea(BaseModel):
    id: int
    titulo: str
    completada: bool = False

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensaje": "API de tareas funcionando"}

@app.post("/tareas", response_model=Tarea)
def crear_tarea(datos: TareaCrear, db: Session = Depends(get_db)):
    nueva_tarea = models.TareaDB(titulo=datos.titulo, completada=datos.completada)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

@app.get("/tareas", response_model=list[Tarea])
def listar_tareas(db: Session = Depends(get_db)):
    return db.query(models.TareaDB).all()

@app.put("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, datos: TareaCrear, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea.titulo = datos.titulo
    tarea.completada = datos.completada
    db.commit()
    db.refresh(tarea)
    return tarea

@app.delete("/tareas/{tarea_id}")
def borrar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    return {"mensaje": f"Tarea {tarea_id} borrada"}
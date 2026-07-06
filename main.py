from fastapi import FastAPI, HTTPException
from storage import cargar_tareas, guardar_tareas
from crud import *
from models import TareaCreate
import json

app = FastAPI()

tareas = cargar_tareas()

@app.get("/")
def inicio():
    return {"mensaje": "Hola"}

@app.get("/tareas")
def obtener_tareas():
    return cargar_tareas()

@app.get("/tareas/{id}")
def ver_tarea(id:int):
    return obtener_tarea()

@app.get("/tareas_completadas")
def ver_completadas():
    return obtener_completadas()

@app.post("/tareas")
def añadir_tarea(tarea:TareaCreate):
    return crear_tarea(tarea)

@app.put("/tareas/{id}")
def completar(id:int):
    return completar_tarea(id)

@app.delete("/tareas/{id}")
def eliminar_tarea(id:int):
    return borrar_tarea(id)

@app.get("/tareas/buscar/{texto}")
def localizar_tarea(texto:str):
    return buscar_tarea(texto)

@app.patch("/tareas/{id}")
def cambiar_tarea(id: int, tarea:TareaUpdate):
    return actualizar_tarea(id, tarea)

@app.get("/tareas")
def listar_tareas(prioridad:str | None=None):
    return obtener_tarea(prioridad)
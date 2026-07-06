from storage import cargar_tareas, guardar_tareas
from fastapi import FastAPI, HTTPException
from datetime import datetime
from models import TareaCreate,TareaUpdate

def crear_tarea(tarea: TareaCreate):
    tareas=cargar_tareas()
    nuevo_id = max([t["id"] for t in tareas], default=0) + 1

    tarea={
        "id": nuevo_id, 
        "texto":tarea.texto, 
        "prioridad": tarea.prioridad,
        "categoria": tarea.categoria,
        "fecha_creacion": datetime.now().isoformat(),
        "completada": False 
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    return tarea

def obtener_tareas(prioridad:str | None = None):
    tareas=cargar_tareas()
    if prioridad is None:
        return tareas
    return [tarea for tarea in tareas if tarea["prioridad"]==prioridad.value]
    

def obtener_tarea(id:int):
    tareas=cargar_tareas()
    for tarea in tareas:
        if tarea["id"]==id:
            return tarea
    return {"error": "Tarea no encontrada"}

def obtener_completadas():
    tareas_completadas=[]
    tareas=cargar_tareas()
    for tarea in tareas:
        if tarea["completada"]:
            tareas_completadas.append(tarea)
    return tareas_completadas
    #return [tarea for tarea in tareas if tarea["completada"]]

def completar_tarea(id:int):
    tareas=cargar_tareas()
    for tarea in tareas:
        if tarea["id"]==id:
            tarea["completada"]=True
            guardar_tareas(tareas)
            return tarea
    # return {"error":"Tarea no encontrada"}
    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


def borrar_tarea(id:int):
    tareas=cargar_tareas()
    for i, tarea in enumerate(tareas):
        if tarea["id"]==id:
            eliminada=tareas.pop(i)
            guardar_tareas(tareas)
            return eliminada
    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )
    # for i,tarea in enumerate(tareas):
    #     if tarea["id"]==id:
    #         eliminado=tareas.pop(i)
    #         return eliminado


def buscar_tarea(texto:str):
        tareas_texto=[]
        tareas=cargar_tareas()
        for tarea in tareas:
            if texto.lower() in tarea["texto"].lower():
                tareas_texto.append(tarea)
        return tareas_texto
        #return [tarea for tarea in tareas if texto.lower() in tarea["texto"].lower()]


def actualizar_tarea(id:int, datos:TareaUpdate):
    tareas= cargar_tareas()
    for tarea in tareas:
        if tarea["id"]==id:
            datos_enviados= datos.model_dump(exclude_unset=True)
            for clave, valor in datos_enviados.items():
                tarea[clave]= valor
            guardar_tareas(tareas)
            return tarea
    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


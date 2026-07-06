import json
def cargar_tareas():
    try:
        with open("tareas.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open("tareas.json","w") as f:
        json.dump(tareas, f, indent=4)
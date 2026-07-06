from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional

class Prioridad(str, Enum):
    baja="baja"
    media="media"
    alta="alta"

class TareaUpdate(BaseModel):
    texto: Optional[str] = None
    prioridad: Optional[Prioridad] = None
    categoria: Optional[str] = None
    completada: Optional[bool] = None
    
class TareaCreate(BaseModel):
    texto: str = Field(min_length=3, max_length=100)
    prioridad: Prioridad
    categoria:str = Field(..., min_length=3, max_length=30)


    @field_validator("texto")
    @classmethod
    def validar_texto(cls,valor):
        texto=valor.strip()
        
        if not texto :
            raise ValueError("La tarea no puede estar vacia")
        
        if texto[0].isdigit():
            raise ValueError("La tarea no puede comenzar con un digito")

        return texto


    @field_validator("categoria")
    @classmethod
    def validar_categoria(cls, valor):
        categoria= valor.strip()
        if not categoria:
            raise ValueError("La categoria no puede estar vacia")
        return categoria


class Tarea(BaseModel):
    id: int
    texto: str
    prioridad: Prioridad
    categoria: str
    fecha_creacion: datetime
    completada: bool

    # @field_validator("prioridad")
    # @classmethod
    # def validar_prioridad(cls, prioridad):
    #     if prioridad not in ["baja", "media","alta"]:
    #         raise ValueError("La prioridad solo puede ser baja, media o alta")
        
    #     return prioridad


# class TareaUpdate(BaseModel):
#     completada: bool

# class Tarea(BaseModel):
#     id: int
#     texto: str
#     completada: bool
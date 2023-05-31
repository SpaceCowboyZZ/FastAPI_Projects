from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import random

class Sex(str):
    male ='male'.lower()
    female = 'female'.lower()


class Atributos(BaseModel):
    id: Optional[int]
    name: str
    age: int
    sex: Sex
    cor: str
    
app = FastAPI()


atributos_lista = []
@app.post('/animais')
def animais(atributos: Atributos):
    atributos.id = random.randint(1,999999)
    atributos_lista.append(atributos)
    return {'status':'completo'}

@app.get('/animais')
def lista():
    return atributos_lista

@app.get('/animais/{id}')
def get_animal(id: int):
    animal = None
    for atr in atributos_lista: #atr é abreviação de atributos
        if atr.id == id:
            animal = atr
            break
    if animal:
        return animal
    else:
        return {'error':'ID not found'}


# @app.delete('/animais/{id}')
# async def del_animal(id: int):
#     index = atributos_lista.index(next((attr for attr in atributos_lista if attr.id == id), None))
#     if index >= 0:
#         atributos_lista.remove(atributos_lista[index])
#     return {"message": f"Animal with ID {id} was deleted."}

@app.delete('/animais/{id}')
async def del_animal(id: int):
    for i, animal in enumerate(atributos_lista):
        if animal.id == id:
            atributos_lista.pop(i)
    return {'message': f'Animal with ID {id} has been deleted'}
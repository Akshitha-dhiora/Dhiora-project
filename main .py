from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

items=[]

class Item(BaseModel):
    id:int
    name:str
    price:float

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item:Item):
    items.append(item)
    return {"message":"Item added"}

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    for i in range(len(items)):
        if items[i].id==item_id:
            items[i]=item
            return {"message":"Item updated"}
    return {"message":"Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    for i in range(len(items)):
        if items[i].id ==item_id:
            items.pop(i)
            return {"message": "Item deleted"}
    return {"message": "Item not found"}

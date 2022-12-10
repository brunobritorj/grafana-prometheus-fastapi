from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

class Item(BaseModel):
    barcode: int
    name: str
    price: float
    qtd: int

items = [
    {
        'barcode': 100123,
        'name': 'Rice',
        'price': 5.99,
        'qtd' : 15
    },
    {
        'barcode': 100456,
        'name' : 'Bean',
        'price' : 4.99,
        'qtd' : 20
    },
    {
        'barcode': 100789,
        'name' : 'Coffee',
        'price' : 5.30,
        'qtd' : 30
    }
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
def read_item():
    list = []
    for i in items:
        list.append({"barcode": i['barcode'], "name": i['name']})
    return list

@app.get("/items/{barcode}")
def read_item(barcode: int):
    resp = {}
    for i in items:
        if barcode == i['barcode']:
            resp = i
    if resp == {}:
        raise HTTPException(status_code=404, detail="Item not found")
    return resp

@app.post("/items/")
def create_item(item: Item):
    items.append({
        'barcode': item.barcode,
        'name' : item.name,
        'price' : item.price,
        'qtd' : item.qtd
    })
    return item

@app.put("/items/{barcode}")
def update_item(barcode: int, item: Item):
    found = False
    for idx, i in enumerate(items):
        if barcode == i['barcode']:
            found = True
            items[idx]['name'] = item.name
            items[idx]['price'] = item.price
            items[idx]['qtd'] = item.qtd
    if found == False:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{id}")
def delete_item(barcode: int):
    found = False
    for idx, i in enumerate(items):
        if barcode == i['barcode']:
            found = True
            item = items[idx]
            del items[idx]
    if found == False:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)
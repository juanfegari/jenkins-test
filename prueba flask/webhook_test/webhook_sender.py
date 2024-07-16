import requests

url = "http://127.0.0.1:5000/webhook_personas"
print("Sending POST request to", url)
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
},{
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles",
}
#r = requests.post(url, json=data)

url2 ="http://127.0.0.1:5000/webhook_pedidos"
print("Sending POST request to", url2)
data2 = {
    "producto": "Laptop",
    "cantidad": 1,
    "estado": "Enviado",
},{
    "producto": "Mouse",
    "cantidad": 2,
    "estado": "Entregado",
},{
    "producto": "Teclado",
    "cantidad": 3,
    "estado": "Pendiente",
},{
    "producto": "Monitor",
    "cantidad": 4,
    "estado": "Cancelado",
}
r2 = requests.post(url2, json=data2)
print(r2._content)
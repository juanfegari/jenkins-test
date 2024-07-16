from flask import Flask, request
from function1 import Personas, Pedido

app = Flask(__name__)

@app.route('/webhook_personas', methods=['POST'])
def listener():
    data = request.json
    print(data)
    for person in data:
        p = Personas(person["name"], person["age"], person["city"])
        print(p.saludo())

    return "OK"

@app.route('/webhook_pedidos', methods=['POST'])
def listener2():
    data = request.json
    print(data)
    for pedido in data:
        p = Pedido(pedido["producto"], pedido["cantidad"], pedido["estado"])
        print(p.info())

    return "OK"

    
if __name__ == '__main__':
    app.run()

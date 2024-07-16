from flask import Flask, Blueprint

calculator_blueprint = Blueprint('calculator', __name__)

@calculator_blueprint.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@calculator_blueprint.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@calculator_blueprint.route('/')
def index():
    return 'Calculator Home'
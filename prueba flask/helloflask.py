from flask import Flask, request, render_template
from blueprints.calculator_bp.calculator_blueprint import calculator_blueprint
from blueprints.login_bp.login_bp import auth_bp

app = Flask(__name__)
app.register_blueprint(calculator_blueprint, url_prefix='/calculator')
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)

@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
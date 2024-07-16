from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Procesar los datos del formulario
        username = request.form['username']
        password = request.form['password']
        # Aquí iría la lógica de autenticación
        return f'Logged in as {username}, password: {password}'
    return render_template('templates.login.html')
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap5

import unittest

from app import create_app

app = create_app()



app.config['SECRET_KEY'] = 'SUPER SECRETO'
todos = ['Adolfo', 'Carlos', 'Daniel', 'Erika', 'Marisol <3', 'Vanessa']


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contrasenia', validators=[DataRequired()])
    SubmitField = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html', error=error)   

@app.errorhandler(500)
def server_error(error):
    return render_template("error_500.html", error=error)

@app.route('/')
def cookie():
    user_ip = request.remote_addr
    response = make_response(redirect('/get_ip'))
    session['user_ip'] = user_ip

    return response

@app.route('/get_ip', methods=['GET', 'POST'])
def marisol():
    user_ip = session.get('user_ip')    
    login_form = LoginForm() 
    username = session.get('username')
    
    context = {
        'todos' : todos,
        'user_ip': user_ip,
        'login_form':login_form,
        'username':username

    }

    if request.method == 'POST':
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito!')
        return redirect(url_for('cookie'))

    return render_template('ip.html', **context)

@app.route('/index')
def index():
    return render_template('inicio.html')

@app.route('/friends')
def amigos():
    context = {
        'todos' : todos
    }
    #expande las variables cuando le colocamos ** 
    return render_template('friends.html', **context)

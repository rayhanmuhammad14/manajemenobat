from flask import Flask, render_template, session, redirect, url_for, flash
from backend.query import login
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'HALLO'
app.permanent_session_lifetime = timedelta(days=1)

msg = ""

@app.route('/', methods = ['POST', 'GET'])
def index():
    return login()
    
@app.route('/home')
def home():
    if 'user' in session:
        return "OKEE"
    flash('Harap Login Terlebih Dahalu', 'info')
    msg = "Harap Login Terlebih Dahulu"
    return render_template('index.html', msg = msg)

@app.errorhandler(404)
def invalid(e):
    msg = "Maaf Sepertinya Urlnya Salah"
    return render_template('404.html', msg=msg)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))
    flash('Harap Login Terlebih Dahalu', 'info')
    msg = "Harap Login Terlebih Dahulu"
    return render_template('index.html', msg = msg)


if '__main__' == __name__:
    app.run(debug=True)
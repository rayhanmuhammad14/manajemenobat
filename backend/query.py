from backend.database import userDatas
from flask import render_template, request, url_for, redirect, session, flash

def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        
        findUsername = userDatas.find_one({'username':username})
        findPassword = userDatas.find_one({'password':password})
        
        if findUsername and findPassword:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash('Kata Sandi Salah','info')
            msg = "USERNAME ATAU PASSWORD SALAH"
            return render_template('index.html', msg = msg)
    return render_template('index.html')
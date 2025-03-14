from flask import Flask, render_template, session, redirect, url_for, flash, jsonify, request
from backend.query import login
from datetime import timedelta
from backend.database import obatDatas, pendapatanDatas

app = Flask(__name__)
app.secret_key = 'HALLO'
app.permanent_session_lifetime = timedelta(days=1)
msg = ""

@app.route('/', methods = ['POST', 'GET'])
def index():
    return login()
    
@app.route('/home', methods = ['POST','GET'])
def home():
    if 'user' in session:
        if request.method == 'POST':
            data = request.get_json()
            dataObat = data.get('dataObat', [])  # Ambil data dari request

            if not dataObat:
                return jsonify({"message": "Data tidak boleh kosong"})

        # Simpan ke database
            pendapatanDatas.insert_many(dataObat)
            return jsonify({"message": "Data berhasil disimpan!"})
        
        dataObat = obatDatas.find({},{"_id":0})
        
        return render_template('home.html', dataObat=dataObat)
    flash('Harap Login Terlebih Dahalu', 'info')
    msg = "Harap Login Terlebih Dahulu"
    return render_template('index.html', msg = msg)

@app.route("/api/obat", methods=["GET"])
def get_obat():
    dataObat = list(obatDatas.find({}, {"_id": 0, "obat": 1, "harga": 1}))
    return jsonify(dataObat)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))
    flash('Harap Login Terlebih Dahalu', 'info')
    msg = "Harap Login Terlebih Dahulu"
    return render_template('index.html', msg = msg)

@app.errorhandler(404)
def invalid(e):
    msg = "Maaf Sepertinya Urlnya Salah"
    return render_template('404.html', msg=msg)

if '__main__' == __name__:
    app.run(debug=True)
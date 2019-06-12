from flask import Flask, render_template, flash, request, url_for, redirect,session
from dbconnection import connection
from passlib.hash import sha256_crypt
import gc
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'redsfsfsfsfis'
socketio = SocketIO(app)
@socketio.on('disconnect')
def disconnect_user():
    session.clear()
@app.route("/")
def homepage():
    session.clear()

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")
@app.route("/home",methods=['GET','POST'])
def login():
    
    c,conn = connection()
   
    try:
        
        if request.method == "POST" :
            print('req')
            if 'submit' in request.form:
                print('sub')
                c.execute("SELECT * FROM users WHERE id = ('%s')" %request.form["id"])
               
                data = c.fetchone()
                print(data)
                if sha256_crypt.verify(request.form['password'],data[1] ):
                    c.close()
                    session['logged_in'] = True
                    session['username'] = request.form['id']
                    conn.commit()
                    conn.close()
                    gc.collect()
                    return render_template("home.html")
    except Exception as e:
        print(e)
        return render_template("login.html")
    print('return')
    return render_template("login.html")
if __name__ == "__main__":
    app.secret_key="bvcfest2k19"
    
    app.run(debug=True)
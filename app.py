from flask import Flask, render_template, flash, request, url_for, redirect,session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'redsfsfsfsfis'
@app.route("/")
def homepage():
    
    return render_template("login.html")
if __name__ == "__main__":
    app.secret_key="bvcfest2k19"
    
    app.run(debug=True)
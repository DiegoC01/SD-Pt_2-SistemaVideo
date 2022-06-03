from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "01011001"

@app.route("/hello")
def index():
    flash("¿Cómo te llamas?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    #nombre del botón en html: name_input
    flash("Hola "+str(request.form['name_input']) + ", ¿cómo estás?")
    return render_template("index.html")

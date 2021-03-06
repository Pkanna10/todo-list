from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Global variable todos
todos = []

@app.route("/")
def tasks():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")
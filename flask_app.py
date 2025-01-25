# flask --app server --debug run
from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {"title": "Главная", "URL": "/"},
    {"title": "iPhone", "URL": "/iphone"},
    {"title": "iPad", "URL": "/ipad"},
    {"title": "MacBook", "URL": "/macbook"},
    {"title": "Об авторе", "URL": "/about"},
    {"title": "Словарь", "URL": "/glossary"},
]

@app.context_processor
def global_context():
    return{
        "nav":nav
    }

@app.route("/")
def main_view():
    #return "<b>Всем привет!</b>"
    return render_template("index.html", name="Главная")

@app.route("/about")
def about_view():
    return render_template("author.html", name="Об авторе")

@app.route("/iphone")
def iphone_view():
    return render_template("iphone.html", name="iPhone")

@app.route("/ipad")
def ipad_view():
    return render_template("ipad.html", name="iPad")

@app.route("/macbook")
def macbook_view():
    return render_template("macbook.html", name="MacBook")

@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html", name="Словарь")
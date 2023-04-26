from flask import Flask, render_template
from mongoengine import connect, Document, StringField, DateTimeField, ListField

    

# Conecta ao banco de dados MongoDB hospedado no Atlas
connect(host='mongodb+srv://vinicius:vinicius1105@cluster0.axbfq4m.mongodb.net/test')

class Projeto(Document):
    nome_do_projeto = StringField(required=True)
    data_de_entrega = DateTimeField(required=True)
    lider = StringField(required=True)
    integrantes = ListField(StringField())


app = Flask(__name__)

#criando uma rota com o decorerator para a página inicial
@app.route("/login")
def login():
    return render_template("templatelogin.html")

@app.route("/usuarios")
def usuario():
    return render_template("templateusuario.html")

@app.route("/tarefas")
def tarefa():
    return render_template("templatetarefa.html")

@app.route("/projetos")
def projeto():
    return render_template("templatetarefa.html")

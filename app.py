from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    nome_capturado = None
    idade_capturada = None
    
    if request.method == "POST":
        nome_capturado = request.form.get("nome")
        idade_capturada = request.form.get("idade")
        novo_usuario = Usuario(nome=nome_capturado, idade=idade_capturada)
        db.session.add(novo_usuario)
        db.session.commit()

    

        print(f"Nome recebido: {nome_capturado}")
        print(f"Idade recebida: {idade_capturada}")

    lista_do_banco = Usuario.query.all()
    return render_template("index.html", nome_no_html=nome_capturado, idade_no_html=idade_capturada, usuarios=lista_do_banco)

if __name__ == "__main__":
    app.run(debug=True)
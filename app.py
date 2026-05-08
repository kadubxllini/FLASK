from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nome_capturado = None
    
    if request.method == "POST":
        nome_capturado = request.form.get("nome")
        print(f"Nome recebido: {nome_capturado}")
    
    return render_template("index.html", nome_no_html=nome_capturado)

if __name__ == "__main__":
    app.run(debug=True)
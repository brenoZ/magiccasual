from flask import Flask, render_template

app = Flask(__name__)

# route -> magicraiz.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/") #atribui nova função ao def da linha seguinte
def homepage():
    return render_template("homepage.html")

@app.route("/decks") #atribui nova função ao def da linha seguinte
def decks():
    return render_template("decks.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

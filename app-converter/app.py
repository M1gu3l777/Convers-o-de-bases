
from flask import Flask, render_template, request
from conversoes import converter

app = Flask(__name__)

NOMES_BASES = {
    2: "Binário",
    8: "Octal",
    10: "Decimal",
    16: "Hexadecimal"
}


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/integrantes")
def integrantes():
    return render_template("integrantes.html")


@app.route("/converter", methods=["GET", "POST"])
def pagina_converter():
    dados = {}

    if request.method == "POST":
        numero = request.form.get("numero", "").strip()
        origem_texto = request.form.get("origem", "")
        destino_texto = request.form.get("destino", "")

        try:
            origem = int(origem_texto)
            destino = int(destino_texto)

            if origem not in NOMES_BASES or destino not in NOMES_BASES:
                raise ValueError("Selecione bases válidas.")

            if not numero:
                raise ValueError("Digite um número para converter.")

            resultado = converter(numero, origem, destino)

            dados = {
                "resultado": resultado,
                "numero_original": numero.upper(),
                "base_origem": NOMES_BASES[origem],
                "base_destino": NOMES_BASES[destino],
                "origem_selecionada": origem_texto,
                "destino_selecionado": destino_texto
            }

        except ValueError as erro:
            dados["erro"] = str(erro)
            dados["numero_digitado"] = numero
            dados["origem_selecionada"] = origem_texto
            dados["destino_selecionado"] = destino_texto

    return render_template("converter.html", **dados)


if __name__ == "__main__":
    app.run(debug=True)

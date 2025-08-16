from flask import Flask, render_template, request, session, redirect, url_for
import random
from ollama_client import generar_respuesta

app = Flask(__name__)
app.secret_key = "super_clave_123"

# Frases motivacionales disponibles
PROMPTS_MOTIVACIONALES = [
    "Dame una frase motivacional corta",
    "Inspírame con una frase positiva",
    "Escríbeme una frase de ánimo para el día",
    "Dame un consejo de superación personal",
    "Dime una frase corta que motive"
]

@app.route("/", methods=["GET", "POST"])
def home():
    if "historial" not in session:
        session["historial"] = []

    if request.method == "POST":
        if "limpiar" in request.form:
            session["historial"] = []
            return redirect(url_for("home"))

        if "motivacion" in request.form:
            prompt = random.choice(PROMPTS_MOTIVACIONALES)
            session["historial"].append({"tipo": "usuario", "contenido": "✨ Frase motivacional"})
        else:
            prompt = request.form.get("prompt", "").strip()
            if prompt:
                session["historial"].append({"tipo": "usuario", "contenido": prompt})

        if prompt:
            respuesta = generar_respuesta(prompt)
            session["historial"].append({"tipo": "asistente", "contenido": respuesta})
            session["historial"] = session["historial"][-20:]  # limitar historial

        session.modified = True

    return render_template("index.html", historial=session["historial"])

if __name__ == "__main__":
    print("🚀 Servidor iniciado en http://127.0.0.1:5000")
    app.run(port=5000, debug=True)

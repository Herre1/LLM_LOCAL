import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma2:2b"

def generar_respuesta(prompt: str) -> str:
    """Consulta el modelo en Ollama y devuelve el texto generado."""
    payload = {"model": MODEL, "prompt": prompt, "stream": True}
    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        if response.status_code != 200:
            return f"Error HTTP {response.status_code}: {response.text}"

        resultado = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    resultado += data["response"]
                if data.get("done", False):
                    break
            except json.JSONDecodeError:
                continue

        return resultado.strip() if resultado else "⚠️ Sin respuesta del modelo."
    except requests.exceptions.ConnectionError:
        return "❌ Error: Ollama no está corriendo en localhost:11434."
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}"
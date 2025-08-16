# 💬 Chat con Gemma 1B - LLM Local

Una aplicación web moderna para chatear con modelos de lenguaje locales usando Ollama y Flask.

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Python 3.8+** instalado en tu sistema
2. **Ollama** ejecutándose localmente en el puerto 11434
3. **Modelo Gemma 3 1B** descargado en Ollama

### Paso 1: Instalar Ollama

```bash
ollama pull gemma3:1b
```

### Paso 2: Clonar el proyecto

```bash
git clone <tu-repositorio>
cd LLM_LOCAL
```

### Paso 3: Instalar dependencias

```bash
pip install flask requests
```

### Paso 4: Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://127.0.0.1:5000**

## 📁 Estructura del Proyecto

```
LLM_LOCAL/
├── app.py                 # Aplicación principal de Flask
├── ollama_client.py       # Cliente para comunicarse con Ollama
├── templates/
│   └── index.html        # Interfaz web del chat
└── README.md             # Este archivo
```

## 🛠️ Uso

### Chat Normal
1. Escribe tu pregunta en el campo de texto
2. Presiona **"Enviar"** o Enter
3. Espera la respuesta del modelo Gemma

### Frases Motivacionales
- Haz clic en **"✨ Motivación"** para recibir una frase inspiradora al instante

### Limpiar Historial
- Usa el botón **"Limpiar"** para borrar todo el historial del chat

## ⚙️ Configuración

### Cambiar el Modelo

Edita el archivo `ollama_client.py`:

```python
MODEL = "gemma2:2b"  # Cambia por tu modelo preferido
```

### Personalizar Puerto

Modifica el archivo `app.py`:

```python
app.run(port=5000, debug=True)  # Cambia el puerto aquí
```

### Ajustar Límite de Historial

En `app.py`, línea 38:

```python
session["historial"] = session["historial"][-20:]  # Máximo 20 mensajes
```
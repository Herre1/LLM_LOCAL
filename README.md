# 💬 Chat con Gemma 2B - LLM Local

Una aplicación web moderna para chatear con modelos de lenguaje locales usando Ollama y Flask.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-Compatible-orange.svg)

## 🌟 Características

- **💻 Chat en tiempo real** con modelos LLM locales
- **✨ Frases motivacionales** con un solo clic
- **🎨 Interfaz moderna** con tema oscuro
- **📱 Diseño responsivo** que se adapta a cualquier pantalla
- **🧹 Historial limpio** con función de borrado
- **⚡ Arquitectura modular** y código bien organizado
- **🔒 Privacidad total** - todo funciona localmente

## 🚀 Instalación y Configuración

### Prerrequisitos

1. **Python 3.8+** instalado en tu sistema
2. **Ollama** ejecutándose localmente en el puerto 11434
3. **Modelo Gemma 2B** descargado en Ollama

### Paso 1: Instalar Ollama

```bash
# Descargar Ollama desde: https://ollama.ai
# Luego instalar el modelo Gemma 2B:
ollama pull gemma2:2b
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

## 🎨 Personalización de la Interfaz

### Colores del Tema

Edita `templates/index.html` para cambiar los colores:

```css
body { 
    background-color: #1e1f26;  /* Fondo principal */
    color: #f5f6fa;             /* Texto principal */
}

.chat-box {
    background: #2a2d38;        /* Fondo del chat */
}

.usuario { 
    background: #4f8cff;        /* Mensajes del usuario */
}

.asistente { 
    background: #3b3f4c;        /* Mensajes del asistente */
}
```

### Agregar Nuevas Frases Motivacionales

En `app.py`, modifica la lista `PROMPTS_MOTIVACIONALES`:

```python
PROMPTS_MOTIVACIONALES = [
    "Dame una frase motivacional corta",
    "Inspírame con una frase positiva",
    "Tu nueva frase aquí",  # Agrega más aquí
]
```

## 🔧 Solución de Problemas

### Error: "Ollama no está corriendo"
```bash
# Verificar que Ollama esté ejecutándose:
ollama serve
```

### Error: "Modelo no encontrado"
```bash
# Instalar el modelo necesario:
ollama pull gemma2:2b
```

### Error de importación
```bash
# Limpiar caché de Python:
rm -rf __pycache__/
```

### Puerto ocupado
- Cambia el puerto en `app.py` a otro disponible (ej: 5001, 8000)

## 🆚 Ventajas sobre Otros Proyectos

✅ **Arquitectura modular** - Código organizado y mantenible  
✅ **Templates separados** - HTML no embebido en Python  
✅ **Múltiples funcionalidades** - Chat + motivación + limpieza  
✅ **Mejor manejo de errores** - Experiencia de usuario robusta  
✅ **Diseño único** - Interfaz personalizada y atractiva  
✅ **Documentación completa** - README detallado  

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de:

1. Hacer fork del proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado con ❤️ para la comunidad de IA local.

---

### 🚀 ¡Disfruta chateando con tu IA local!

Si te gusta este proyecto, ¡dale una ⭐ en GitHub!

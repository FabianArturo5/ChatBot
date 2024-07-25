 <h1>Chatbot AutoMotriz</h1>
¡Bienvenido al proyecto Chatbot AutoMotriz! Este chatbot está diseñado para proporcionar información sobre vehículos, incluyendo modelos, precios y opciones de financiamiento. Utiliza Flask para la interfaz web y NLTK para el procesamiento del lenguaje natural.

## Características

- Responde preguntas sobre modelos de autos y sus precios.
- Proporciona información sobre autos eléctricos y usados.
- Ofrece detalles sobre opciones de financiamiento y garantías.
- Incluye respuestas personalizadas para diferentes consultas relacionadas con vehículos.

## Instalación

Para instalar y ejecutar el chatbot en tu entorno local, sigue estos pasos:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/chatbot-automotriz.git
cd chatbot-automotriz
```
### 2. Crear un Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
```
### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar el Servidor
```bash
python app.py
```
El chatbot estará disponible en http://127.0.0.1:5000/.
Uso
Una vez que el servidor esté en ejecución, abre tu navegador y ve a http://127.0.0.1:5000/. Puedes interactuar con el chatbot a través de la interfaz web.
Cómo Funciona
El chatbot está basado en el módulo nltk.chat de la biblioteca NLTK y está configurado para responder en español. Los pares de preguntas y respuestas están definidos en el archivo app.py. El chatbot utiliza expresiones regulares para identificar la entrada del usuario y proporcionar respuestas adecuadas.
¡Gracias por usar Chatbot AutoMotriz!

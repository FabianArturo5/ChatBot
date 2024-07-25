 <h1>Chatbot AutoMotriz</h1>
¡Bienvenido al proyecto Chatbot AutoMotriz! Este chatbot está diseñado para proporcionar información sobre vehículos, incluyendo modelos, precios y opciones de financiamiento. Utiliza Flask para la interfaz web y NLTK para el procesamiento del lenguaje natural.

Características

    -Responde preguntas sobre modelos de autos y sus precios.
    -Proporciona información sobre autos eléctricos y usados.
    -Ofrece detalles sobre opciones de financiamiento y garantías.
    -Incluye respuestas personalizadas para diferentes consultas relacionadas con vehículos.


<h2>Instalación</h2>
<p>Para instalar y ejecutar el chatbot en tu entorno local, sigue estos pasos:

1. Clonar el Repositorio
<pre><code>git clone https://github.com/tu_usuario/chatbot-automotriz.git
cd chatbot-automotriz

2. Crear un Entorno Virtual
<pre><code>python -m venv venv
source venv/bin/activate # En Windows, usa venv\Scripts\activate

3. Instalar Dependencias
<pre><code>pip install -r requirements.txt
<h2>4. Ejecutar el Servidor</h2>
<pre><code>python app.py
<p>El chatbot estará disponible en <code>http://127.0.0.1:5000/</code>.</p>

Uso
<p>Una vez que el servidor esté en ejecución, abre tu navegador y ve a <code>http://127.0.0.1:5000/</code>. Puedes interactuar con el chatbot a través de la interfaz web.</p>

Cómo Funciona
<p>El chatbot está basado en el módulo <code>nltk.chat</code> de la biblioteca NLTK y está configurado para responder en español. Los pares de preguntas y respuestas están definidos en el archivo <code>app.py</code>. El chatbot utiliza expresiones regulares para identificar la entrada del usuario y proporcionar respuestas adecuadas.</p>


¡Gracias por usar Chatbot AutoMotriz!

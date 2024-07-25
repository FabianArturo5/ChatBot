Chatbot AutoMotriz
¡Bienvenido al proyecto Chatbot AutoMotriz! Este chatbot está diseñado para proporcionar información sobre vehículos, incluyendo modelos, precios y opciones de financiamiento. Utiliza Flask para la interfaz web y NLTK para el procesamiento del lenguaje natural.

Características

    -Responde preguntas sobre modelos de autos y sus precios.
    -Proporciona información sobre autos eléctricos y usados.
    -Ofrece detalles sobre opciones de financiamiento y garantías.
    -Incluye respuestas personalizadas para diferentes consultas relacionadas con vehículos.


<h2>Instalación</h2>
<p>Para instalar y ejecutar el chatbot en tu entorno local, sigue estos pasos:

<h3>1. Clonar el Repositorio</h3>
<pre><code>git clone https://github.com/tu_usuario/chatbot-automotriz.git
cd chatbot-automotriz

<h3>2. Crear un Entorno Virtual</h3>
<pre><code>python -m venv venv
source venv/bin/activate # En Windows, usa venv\Scripts\activate

<h3>3. Instalar Dependencias</h3>
<pre><code>pip install -r requirements.txt
<h3>4. Ejecutar el Servidor</h3>
<pre><code>python app.py
<p>El chatbot estará disponible en <code>http://127.0.0.1:5000/</code>.</p>

<h2>Uso</h2>
<p>Una vez que el servidor esté en ejecución, abre tu navegador y ve a <code>http://127.0.0.1:5000/</code>. Puedes interactuar con el chatbot a través de la interfaz web.</p>

<h3>Cómo Funciona</h3>
<p>El chatbot está basado en el módulo <code>nltk.chat</code> de la biblioteca NLTK y está configurado para responder en español. Los pares de preguntas y respuestas están definidos en el archivo <code>app.py</code>. El chatbot utiliza expresiones regulares para identificar la entrada del usuario y proporcionar respuestas adecuadas.</p>

<h2>Estructura del Proyecto</h2>
<ul>
    <li><code>app.py</code>: Contiene la lógica del chatbot y la configuración del servidor Flask.</li>
    <li><code>templates/index.html</code>: Archivo HTML para la interfaz web.</li>
    <li><code>requirements.txt</code>: Lista de dependencias necesarias para ejecutar el proyecto.</li>
</ul>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Si encuentras errores o deseas añadir nuevas funcionalidades, siéntete libre de abrir un pull request.</p>

<h2>Licencia</h2>
<p>Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo <code>LICENSE</code> para más detalles.</p>

<h2>Contacto</h2>
<p>Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarme a través de <a href="mailto:tuemail@example.com">tu correo electrónico</a>.</p>

<div class="note">
    <p><strong>Nota:</strong> Asegúrate de ajustar los detalles, como el enlace al repositorio, tu nombre de usuario y el correo electrónico, según corresponda.</p>
</div>

<h3>¡Gracias por usar Chatbot AutoMotriz!</h3>

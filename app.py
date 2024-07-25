from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import re

app = Flask(__name__)

# Reflexiones en español
reflections_es = {
    "yo soy": "tú eres",
    "yo": "tú",
    "mi": "tu",
    "mío": "tuyo",
    "tú eres": "yo soy",
    "tú": "yo",
    "tu": "mi",
    "tuyo": "mío"
}

# Pares de preguntas y respuestas en español relacionadas con vehículos
pairs_es = [
    ['mi nombre es (.*)', ['Hola %1, ¿cómo puedo ayudarte hoy?']],
    ['hola|buenas|hey', ['¡Hola!', '¡Hey!', '¡Buenas!']],
    ['como te llamas', ['Soy el Chatbot AutoMotriz, creado por [Tu Nombre].']],
    ['como estas', ['Estoy bien, gracias. ¿Y tú?', '¡Todo bien! ¿Y tú?']],
    ['adios|chau|hasta luego', ['¡Adiós! ¡Cuídate!']],
    ['que modelos de autos tienes', ['Tenemos una amplia gama de modelos, desde sedanes hasta SUVs. ¿Buscas algo en particular?']],
    ['cual es el precio del (.*)', ['El precio del %1 varía según las características y el año del modelo. ¿Te gustaría más información específica?']],
    ['tienes autos electricos', ['Sí, tenemos varios modelos eléctricos disponibles. ¿Te gustaría saber más sobre ellos?']],
    ['cuales son las marcas que manejas', ['Trabajamos con marcas como Toyota, Honda, Ford, y muchas más. ¿Tienes alguna preferencia?']],
    ['tienes autos usados', ['Sí, tenemos una selección de autos usados certificados. ¿Buscas algún modelo o año en particular?']],
    ['(.*)', ['No estoy seguro de cómo responder a eso. ¿Puedes preguntar algo más?']]
]

# Creación del chatbot en español
chat_es = Chat(pairs_es, reflections_es)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["message"]
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)  # Elimina signos de puntuación
    chat_response = chat_es.respond(user_input)
    return jsonify({"response": chat_response})

if __name__ == "__main__":
    app.run(debug=True)
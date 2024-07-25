from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

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

# Pares de preguntas y respuestas en español
pairs_es = [
    ['mi nombre es (.*)', ['Hola %1, ¿cómo puedo ayudarte hoy?']],
    ['hola|buenas|hey', ['¡Hola!', '¡Hey!', '¡Buenas!']],
    ['¿cómo te llamas?', ['Soy un chatbot creado por [Tu Nombre].']],
    ['¿cómo estás?', ['Estoy bien, gracias. ¿Y tú?', '¡Todo bien! ¿Y tú?']],
    ['adiós|chau|hasta luego', ['¡Adiós! ¡Cuídate!']],
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
    chat_response = chat_es.respond(user_input)
    return jsonify({"response": chat_response})

if __name__ == "__main__":
    app.run(debug=True)

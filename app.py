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
    ['como te llamas', ['Soy el Chatbot AutoMotriz, creado por Fabian Martinez.']],
    ['como estas', ['Estoy bien, gracias. ¿Y tú?', '¡Todo bien! ¿Y tú?']],
    ['adios|chau|hasta luego', ['¡Adiós! ¡Cuídate!']],
    ['que modelos de autos tienes', [
        'Contamos con una amplia gama de modelos. Aquí te dejo algunos ejemplos:\n'
        '1. Toyota Camry, '
        '2. Honda CR-V, '
        '3. Ford F-150, '
        '4. Tesla Model 3, '
        '5. Nissan Leaf, '
        '6. BMW Serie 3, '
        '7. Audi A4, '
        '8. Subaru Outback, '
        '9. Mercedes-Benz C-Class, '
        '10. Chevrolet Silverado, '
        '¿Hay algún modelo específico que te interese?, '
    ]],

    ['(.*)toyota camry(.*)', ['El precio del Toyota Camry comienza en aproximadamente $25,000.']],
    ['(.*)honda cr-v(.*)', ['El precio del Honda CR-V empieza desde unos $28,000.']],
    ['(.*)ford f-150(.*)', ['El precio de la Ford F-150 inicia alrededor de $35,000.']],
    ['(.*)tesla model 3(.*)', ['El Tesla Model 3 tiene un precio base de aproximadamente $40,000.']],
    ['(.*)nissan leaf(.*)', ['El Nissan Leaf tiene un precio que comienza en unos $30,000.']],
    ['(.*)bmw serie 3(.*)', ['El precio del BMW Serie 3 comienza en unos $42,000.']],
    ['(.*)audi a4(.*)', ['El precio del Audi A4 empieza desde aproximadamente $45,000.']],
    ['(.*)subaru outback(.*)', ['El precio del Subaru Outback inicia alrededor de $33,000.']],
    ['(.*)mercedes-benz c-class(.*)', ['El precio del Mercedes-Benz C-Class comienza en unos $50,000.']],
    ['(.*)chevrolet silverado(.*)', ['El precio del Chevrolet Silverado empieza desde aproximadamente $32,000.']],
    
    ['tienes autos electricos', ['Sí, ofrecemos varios modelos de autos eléctricos, como el Tesla Model 3 y el Nissan Leaf. ¿Te interesa saber más sobre alguno de estos modelos o tienes otra consulta?']],
    ['cuales son las marcas que manejas', [
        'Trabajamos con marcas reconocidas como: Toyota, Honda, Ford, BMW, Nissan, Audi, Subaru, Mercedes-Benz, Chevrolet, Volkswagen'
    ]],
    ['(.*)autos usados(.*)', ['Sí, tenemos una selección de autos usados certificados. Todos nuestros autos usados pasan por un riguroso control de calidad. ¿Buscas algún modelo o año en particular?']],
    ['(.*)garantia(.*)', ['La garantía de un auto nuevo suele durar entre 3 y 5 años, dependiendo de la marca y el modelo. Por ejemplo, Toyota ofrece una garantía de 3 años o 36,000 millas. ¿Te gustaría conocer la garantía específica de algún vehículo?']],
    ['(.*)financiar(.*)', ['Ofrecemos varias opciones de financiamiento para facilitar la compra de tu vehículo. Puedes optar por financiamiento a través de bancos asociados o planes internos de la concesionaria. ¿Te gustaría saber más sobre alguna de estas opciones?']],
    ['que debo considerar al comprar un auto usado', ['Al comprar un auto usado, es importante revisar el historial del vehículo, verificar el estado general y realizar una prueba de manejo. También es recomendable obtener una inspección profesional. ¿Te gustaría saber más sobre alguno de estos puntos?']],
    ['(.*)mantenimientos necesitan los autos electricos', ['Los autos eléctricos requieren menos mantenimiento que los autos con motor de combustión. Sin embargo, es importante revisar periódicamente la batería, el sistema de frenos y los neumáticos. Además, algunos fabricantes recomiendan revisiones anuales. ¿Te gustaría saber más sobre el mantenimiento de un modelo específico?']],
    ['(.*)', ['No estoy seguro de cómo responder a eso. ¿Puedes preguntar algo más relacionado con vehículos?']]
]




# Creación del chatbot en español
chat_es = Chat(pairs_es, reflections_es)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get('message').lower()
    if not user_input:
        return jsonify({'response': 'No se recibió ningún mensaje.'})

    # Buscar una respuesta adecuada para la entrada del usuario
    chat_response = chat_es.respond(user_input)
    # Si la respuesta es None (no se encontró coincidencia), usar una respuesta por defecto
    if not chat_response:
        chat_response = 'No estoy seguro de cómo responder a eso. ¿Puedes preguntar algo más relacionado con vehículos?'
        
    return jsonify({'response': chat_response})

if __name__ == "__main__":
    app.run(debug=True)
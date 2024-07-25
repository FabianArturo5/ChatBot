import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk

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
    ['como te llamas', ['Soy un chatbot creado por [Tu Nombre].']],
    ['como estas', ['Estoy bien, gracias. ¿Y tú?', '¡Todo bien! ¿Y tú?']],
    ['adios|chau|hasta luego', ['¡Adiós! ¡Cuídate!']],
    ['(.*)', ['No estoy seguro de cómo responder a eso. ¿Puedes preguntar algo más?']]
]

# Creación del chatbot en español
chat_es = Chat(pairs_es, reflections_es)

# Función para iniciar una conversación en la terminal
def start_terminal_chat():
    print("¡Hola! Soy un chatbot. Escribe 'adiós' para salir.")
    chat_es.converse()

# Función para iniciar una conversación en una interfaz gráfica
def start_gui_chat():
    def send_message():
        user_input = entry.get()
        if user_input.lower() in ['adiós', 'chau', 'hasta luego']:
            root.quit()
        else:
            chat_response = chat_es.respond(user_input)
            chat_log.config(state=tk.NORMAL)
            chat_log.insert(tk.END, "Tú: " + user_input + "\n")
            chat_log.insert(tk.END, "Bot: " + chat_response + "\n")
            chat_log.config(state=tk.DISABLED)
            entry.delete(0, tk.END)
    
    root = tk.Tk()
    root.title("Chatbot")

    chat_log = tk.Text(root, state=tk.DISABLED)
    chat_log.pack()

    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Return>", lambda event: send_message())
    
    send_button = tk.Button(root, text="Enviar", command=send_message)
    send_button.pack()

    root.mainloop()

# Ejecución del chatbot en terminal o GUI
if __name__ == "__main__":
    mode = input("Ingresa '1' para chat en terminal, '2' para chat en GUI: ")
    if mode == '1':
        start_terminal_chat()
    elif mode == '2':
        start_gui_chat()
    else:
        print("Opción no válida. Por favor ingresa '1' o '2'.")

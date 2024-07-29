import tkinter as tk
from openai import OpenAI

# Configura el cliente de OpenAI (asegúrate de proteger tu clave de API)
client = OpenAI(api_key="sk-None-OoMEjKU888ClGXIKEQDJT3BlbkFJKwHWkBayyes0UcerzZCi")

def on_send_click():
    user_input = text_box.get("1.0", tk.END).strip()  # Obtiene y limpia el texto del campo de texto
    if user_input:
        # Define el prompt con la instrucción de límite de caracteres y las instrucciones del GPT
        prompt = (
            "Este GPT está diseñado para asistir a estudiantes universitarios en la gestión de su tiempo en proyectos y tareas escolares. "
            "Solo responderás a consultas relacionadas con la educación y la organización académica.\n\n"
            "Áreas de Asistencia:\n"
            "1. Gestión del Tiempo: Ayuda con la planificación de horarios y la organización de tareas.\n"
            "2. Planificación de Proyectos: Asiste en la división de proyectos en tareas y el establecimiento de plazos.\n"
            "3. Consejos de Estudio: Proporciona estrategias para mejorar la eficacia del estudio.\n"
            "4. Monitoreo del Progreso: Ofrece recomendaciones para el seguimiento del avance en tareas y proyectos.\n\n"
            "Responde de manera enfocada en temas educativos y la gestión del tiempo académico. No respondas preguntas sobre temas fuera del ámbito educativo.\n\n"
            f"Consulta: {user_input}\n\nResponde con un máximo de 250 caracteres."
        )
        
        # Define el historial de mensajes
        messages = [{"role": "user", "content": prompt}]
        
        # Solicita una respuesta al modelo de OpenAI
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",  # Asegúrate de que el nombre del modelo sea correcto
                messages=messages,
            )
            bot_response = completion.choices[0].message.content
            response_label.config(text=bot_response)  # Actualiza la etiqueta con la respuesta
        except Exception as e:
            response_label.config(text=f"Error: {e}")
    else:
        response_label.config(text="Por favor, ingresa un mensaje.")

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz de Chat con OpenAI")

# Crear el campo de texto
text_box = tk.Text(window, height=5, width=40)
text_box.pack()

# Crear el botón de enviar
send_button = tk.Button(window, text="Enviar", command=on_send_click)
send_button.pack()

# Crear una etiqueta para mostrar la respuesta
response_label = tk.Label(window, text="")
response_label.pack()

# Ejecutar el bucle principal de la interfaz
window.mainloop()

import tkinter as tk
from openai import OpenAI

# Configura el cliente de OpenAI (asegúrate de proteger tu clave de API)
client = OpenAI(api_key="")

def on_send_click():
    user_input = text_box.get("1.0", tk.END).strip()  # Obtiene y limpia el texto del campo de texto
    if user_input:
        # Define el prompt con la instrucción de límite de caracteres
        prompt = f"{user_input}\n\nResponde con un máximo de 100 caracteres."
        
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

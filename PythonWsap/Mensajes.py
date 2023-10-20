import tkinter as tk
from twilio.rest import Client

# Función para enviar el mensaje
def enviar_mensaje():
    account_sid = 'AC4c7212a48410e9a8c36a121ff6b551a7'
    auth_token = 'a872a73f20f7f9570e54d6edfa52949e'
    
    numero_destino = numero_entry.get()
    mensaje = mensaje_text.get("1.0", "end-1c")
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensaje,
        to=f'whatsapp:{numero_destino}'
    )
    
    resultado_label.config(text=f'Mensaje enviado: {message.sid}')

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Enviar Mensaje por WhatsApp")

# Etiqueta y entrada para el número de destino
numero_label = tk.Label(ventana, text="Número de WhatsApp:")
numero_label.pack()
numero_entry = tk.Entry(ventana)
numero_entry.pack()

# Etiqueta y entrada para el mensaje
mensaje_label = tk.Label(ventana, text="Mensaje:")
mensaje_label.pack()
mensaje_text = tk.Text(ventana, height=5, width=30)
mensaje_text.pack()

# Botón para enviar el mensaje
enviar_boton = tk.Button(ventana, text="Enviar Mensaje", command=enviar_mensaje)
enviar_boton.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()

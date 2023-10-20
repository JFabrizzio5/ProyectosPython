# -*- coding: utf-8 -*-

# Importa las bibliotecas necesarias
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import time

# Función para reiniciar MongoDB usando el comando systemctl de Linux.
def restart_mongodb():
    try:
        # Ejecuta el comando para reiniciar MongoDB usando sudo
        subprocess.run(["sudo", "systemctl", "restart", "mongodb"], check=True)
        print("MongoDB reiniciado correctamente.")
        return True  # Retorna True si MongoDB se reinicia correctamente
    except subprocess.CalledProcessError as e:
        print(f"Error al reiniciar MongoDB: {e}")
        return False  # Retorna False si hay un error al reiniciar MongoDB

# Configuración para el servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Puerto estándar para TLS

# Tu dirección de correo y contraseña (reemplázalas por tus propias credenciales)
smtp_username = 'Josephfabrizizo@gmail.com'
smtp_password = 'uftr oavl byqr bvde'  # Reemplaza 'tu_contraseña' con tu contraseña real

# Enviar correo de notificación al iniciar la ejecución
inicio_msg = MIMEMultipart()
inicio_msg['From'] = 'Josephfabrizizo@gmail.com'
inicio_msg['To'] = 'tecnologia@jmbcontadores.mx'
inicio_msg['Subject'] = 'Iniciando ejecucin del script'
inicio_content = 'El script se ha iniciado correctamente.'
inicio_msg.attach(MIMEText(inicio_content, 'plain'))

# Iniciar la conexión SMTP y enviar el correo de notificación de inicio
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Inicia una conexión TLS segura
    server.login(smtp_username, smtp_password)
    server.sendmail(inicio_msg['From'], inicio_msg['To'], inicio_msg.as_string())

# Número máximo de ejecuciones
max_ejecuciones = 7

# Inicializa el contador de ejecuciones
contador_ejecuciones = 0

# Bucle para ejecutar el script cada 15 minutos y limitarlo a 7 veces
while contador_ejecuciones < max_ejecuciones:
    # Obtiene información sobre el uso de la memoria RAM en GB
    ram = psutil.virtual_memory()
    ram_usada_gb = ram.used / (1024 ** 3)  # Convertir bytes a GB
    ram_falta_gb = ram.free / (1024 ** 3)  # Convertir bytes a GB

    # Registra la hora actual
    hora_actual = time.strftime("%Y-%m-%d %H:%M:%S")

    # Crea el objeto MIMEMultipart
    msg = MIMEMultipart()

    # Detalles del correo con información de la RAM en el asunto
    msg['From'] = 'Josephfabrizizo@gmail.com'
    msg['To'] = 'tecnologia@jmbcontadores.mx'

    # Verifica si se debe reiniciar MongoDB y envía correo de notificación
    if ram_falta_gb <= 3:
        if restart_mongodb():
            subject = 'SE REINICIÓ MONGO - Historial Uso de RAM'
        else:
            subject = 'ERROR al reiniciar MongoDB - Historial Uso de RAM'
    else:
        subject = 'Historial Uso de RAM'

    msg['Subject'] = subject

    # Contenido HTML con estilo y especificación de conjunto de caracteres UTF-8
    html_content = f"""
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
      body {{
        font-family: Arial, sans-serif;
      }}
      .container {{
        width: 80%;
        margin: 0 auto;
      }}
      .header {{
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 1em;
      }}
      .content {{
        margin-top: 20px;
      }}
      .usage-info {{
        font-size: 18px;
        color: #007bff;
      }}
    </style>
    </head>
    <body>
    <div class="container">
      <div class="header">
        <h1>Historial de Uso de RAM</h1>
      </div>
      <div class="content">
        <p class="usage-info">Hora: {hora_actual}</p>
        <p class="usage-info">Uso del sistema de RAM: {ram_usada_gb:.2f} GB</p>
        <p class="usage-info">RAM disponible: {ram_falta_gb:.2f} GB</p>
      </div>
    </div>
    </body>
    </html>
    """

    # Adjunta el contenido HTML al mensaje
    msg.attach(MIMEText(html_content, 'html'))

    # Inicia la conexión SMTP y envía el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Inicia una conexión TLS segura
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())

    # Incrementa el contador de ejecuciones
    contador_ejecuciones += 1

    # Espera 15 minutos antes de la próxima ejecución
    if contador_ejecuciones < max_ejecuciones:
        time.sleep(900)  # 900 segundos = 15 minutos

# Muestra un mensaje indicando que el proceso ha terminado
print('El proceso ha terminado. Se han realizado 7 ejecuciones.')

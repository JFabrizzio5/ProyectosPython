import requests

# URL de la API
url = 'http://open-assistant.io'

# Texto a ser analizado por la API
text = input("Cualquier texto: ")

# Datos a enviar en el cuerpo del mensaje POST
data = {'prompt': text}

# Enviando solicitud POST a la API
response = requests.post(url, json=data)

# Comprobar si existe una respuesta
if response.status_code == 200:
    # Obtener los datos de la respuesta
    data = response.json()
    
    # Imprimir el resultado obtenido
    print('Resultados: ', data['choices'][0]['text'])
else:
    # Mostrar error al no recibir ningún tipo de información desde la API
    print('Error al contactar a Open Assistant')

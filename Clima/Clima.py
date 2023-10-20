import requests

# Definir la URL de la API y los parámetros de la solicitud
url = 'https://api.tomorrow.io/v4/timelines'
params = {
    'location': 'CDMX',  # Cambia 'Ciudad de México' por la ciudad que desees
    'fields': 'temperature',
    'timesteps': '1h',
    'units': 'metric',
    'apikey': 'VYbPgfXtAwSU9yCofHRSu1N2wSTyWseG'
}

# Realizar la solicitud HTTP GET
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Imprimir la temperatura actual
    temperature = data['data']['timelines'][0]['intervals'][0]['values']['temperature']
    print(f"La temperatura en {params['location']} es {temperature} °C")
else:
    print(f"Error al obtener el clima. Código de estado: {response.status_code}")

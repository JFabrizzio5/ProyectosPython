import requests
import json

# URL de tu API
api_url = 'https://jos5web.000webhostapp.com/indexx.php'

# Realizar una solicitud GET para obtener datos
def get_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            print(item)
    else:
        print("Error al obtener datos:", response.status_code)

# Realizar una solicitud POST para crear un nuevo registro
def create_data():
    new_data = {
        "Id_Usu": "1",
        "Id_Usu2": "2",
        "Mensaje": "Nuevo mensaje desde Python"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, data=json.dumps(new_data), headers=headers)
    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error al crear nuevo registro:", response.status_code)

# Realizar una solicitud PUT para editar un registro existente
def edit_data(new_message):
    url = "https://jos5web.000webhostapp.com/put.php"  # URL de tu servidor PHP

    data = {
        "Mensaje": new_message
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.put(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Captura excepciones de solicitud HTTP
        if response.status_code == 200:
            print("Registros actualizados exitosamente.")
        else:
            print("Error al actualizar los registros:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)



# Menú de selección de acción
while True:
    print("Selecciona una acción:")
    print("1. Realizar una operación GET")
    print("2. Realizar una operación POST")
    print("3. Realizar una operación PUT")
    print("4. Salir")
    
    choice = input("Elije una opción (1/2/3/4): ")

    if choice == '1':
        get_data()
    elif choice == '2':
        create_data()
   # Luego, en el menú de selección de acciones, puedes llamar a la función edit_data sin proporcionar un ID de chat específico:
    elif choice == '3':
            new_message = input("Ingrese el nuevo mensaje: ")
            edit_data(new_message)
    elif choice == '4':
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

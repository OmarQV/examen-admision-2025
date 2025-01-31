import requests
from datetime import datetime

BASE_URL = "http://localhost:5000/api"
headers = {"Content-Type": "application/json"}

# Crear un nuevo préstamo
print("\n--------- NUEVO PRÉSTAMO ---------")
url = f"{BASE_URL}/prestamos"
prestamo = {
    "usuario_id": 1,
    "libro_id": 1,
    "fecha_prestamo": datetime.now().date().isoformat(),
}
response = requests.post(url, json=prestamo, headers=headers)
print("Creando un nuevo préstamo...")
print(response.json())

# Obtener lista de préstamos
print("\n--------- LISTA DE PRÉSTAMOS ---------")
url = f"{BASE_URL}/prestamos"
response = requests.get(url, headers=headers)
print(response.json())

# Obtener un préstamo específico
print("\n--------- PRÉSTAMO ID: 1 ---------")
url = f"{BASE_URL}/prestamos/1"
response = requests.get(url, headers=headers)
print(response.json())

# Actualizar un préstamo
print("\n--------- UPDATE PRÉSTAMO ID: 1 ---------")
url = f"{BASE_URL}/prestamos/1"
prestamo_update = {
    "usuario_id": 1,
    "libro_id": 1,
    "fecha_prestamo": datetime.now().date().isoformat(),
    "fecha_devolucion": None,
    "estado": "devuelto"
}
response = requests.put(url, json=prestamo_update, headers=headers)
print(response.json())

# Eliminar un préstamo
print("\n--------- DELETE PRÉSTAMO ID: 1 ---------")
url = f"{BASE_URL}/prestamos/1"
response = requests.delete(url, headers=headers)
if response.status_code == 204:
    print("Préstamo eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")

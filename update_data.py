import requests
import csv
import json

# 1. La URL de tu Google Sheet
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRHdenGvzR7M1gFEEjoEYsOHyBrBtkPtjF7OXLkCInCqI8RpnF13L198mls0B9VqMYhDbo_--pW68DB/pub?gid=0&single=true&output=csv'

# --- INICIO DE LA CORRECCIÓN ---
# 2. Nos "disfrazamos" de un navegador para que Google no nos bloquee.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# --- FIN DE LA CORRECCIÓN ---

# 3. Descargar el contenido del CSV, pero usando el disfraz.
print("Descargando datos desde Google Sheets...")
# Añadimos 'headers=headers' a la petición
response = requests.get(CSV_URL, headers=headers) 
response.raise_for_status()  # Se asegura de que la descarga fue exitosa
csv_content = response.content.decode('utf-8')

# 4. Leer el CSV y convertirlo a una lista de diccionarios
csv_reader = csv.DictReader(csv_content.splitlines())
data_list = list(csv_reader)

# 5. Guardar los datos en el archivo datos.json
output_path = 'data/datos.json'
print(f"Guardando {len(data_list)} registros en {output_path}...")
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)

print("¡Actualización completada con éxito!")

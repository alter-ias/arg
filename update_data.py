import requests
import csv
import json

# 1. La URL original de tu Google Sheet
original_sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRHdenGvzR7M1gFEEjoEYsOHyBrBtkPtjF7OXLkCInCqI8RpnF13L198mls0B9VqMYhDbo_--pW68DB/pub?gid=0&single=true&output=csv'

# 2. Creamos la URL del proxy, que actuará como intermediario
# Usamos corsproxy.io, que es el que funcionó en la web.
PROXY_URL = f"https://corsproxy.io/?{original_sheet_url}"

# 3. Descargar el contenido del CSV a través del proxy.
# Ya no necesitamos el "disfraz" (headers) porque el proxy lo hace por nosotros.
print(f"Descargando datos a través del proxy desde: {PROXY_URL}")
response = requests.get(PROXY_URL)
response.raise_for_status()  # Se asegura de que la descarga fue exitosa
csv_content = response.content.decode('utf-8')

# 4. Leer el CSV y convertirlo a una lista de diccionarios
print("Parseando el contenido CSV...")
csv_reader = csv.DictReader(csv_content.splitlines())
data_list = list(csv_reader)

# 5. Guardar los datos en el archivo datos.json
output_path = 'data/datos.json'
print(f"Guardando {len(data_list)} registros en {output_path}...")
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)

print("¡Actualización completada con éxito!")

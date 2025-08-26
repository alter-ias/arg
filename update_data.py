import requests
import csv
import json

# 1. La URL de tu Google Sheet (la que publicaste como CSV)
# Asegúrate de que siga siendo pública para que el script pueda acceder a ella.
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRHdenGvzR7M1gFEEjoEYsOHyBrBtkPtjF7OXLkCInCqI8RpnF13L198mls0B9VqMYhDbo_--pW68DB/pub?gid=0&single=true&output=csv'

# 2. Descargar el contenido del CSV
print("Descargando datos desde Google Sheets...")
response = requests.get(CSV_URL)
response.raise_for_status()  # Se asegura de que la descarga fue exitosa
csv_content = response.content.decode('utf-8')

# 3. Leer el CSV y convertirlo a una lista de diccionarios (objetos)
# csv.DictReader usa la primera fila como las claves, ¡justo lo que necesitamos!
csv_reader = csv.DictReader(csv_content.splitlines())
data_list = list(csv_reader)

# 4. Guardar los datos en el archivo datos.json
output_path = 'data/datos.json'
print(f"Guardando {len(data_list)} registros en {output_path}...")
with open(output_path, 'w', encoding='utf-8') as json_file:
    # ensure_ascii=False para que guarde correctamente acentos, eñes, etc.
    # indent=2 para que el archivo sea legible por humanos.
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)

print("¡Actualización completada con éxito!")

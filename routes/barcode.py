import urllib.request
import json
import pprint

API_KEY = "qpcp9yxlg8dnv28bfhvy78ex7l1ml9"

def obtener_datos_codigo_barras(code):
    url = f"https://api.barcodelookup.com/v3/products?barcode={code}&formatted=y&key={API_KEY}"
    
    try:
        with urllib.request.urlopen(url) as respuesta:
            datos = json.loads(respuesta.read().decode())
            
            # Procesar datos
            codigo_barras = datos["products"][0]["barcode_number"]
            nombre = datos["products"][0]["title"]            
            return datos  
    
    except urllib.error.URLError as e:
        print("Error al obtener datos:", e)


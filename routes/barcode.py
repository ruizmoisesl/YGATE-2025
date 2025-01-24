import urllib.request
import json
import pprint

API_KEY = "qpcp9yxlg8dnv28bfhvy78ex7l1ml9"

def obtener_datos_codigo_barras(code=7707228547906):
    url = f"https://api.barcodelookup.com/v3/products?barcode={code}&formatted=y&key={API_KEY}"
    
    try:
        with urllib.request.urlopen(url) as respuesta:
            datos = json.loads(respuesta.read().decode())
            
            # Imprimir los datos completos para verificar la respuesta
            pprint.pprint(datos)
            
            # Procesar datos
            if "products" in datos and len(datos["products"]) > 0:
                codigo_barras = datos["products"][0]["barcode_number"]
                nombre = datos["products"][0]["title"]
                return datos, nombre, codigo_barras
            else:
                print("No se encontraron productos en la respuesta.")
                return None, None, None
    
    except urllib.error.URLError as e:
        print("Error al obtener datos:", e)
        return None, None, None

# Ejemplo de uso
datos, nombre, codigo_barras = obtener_datos_codigo_barras()
print(f"Nombre: {nombre}, Código de barras: {codigo_barras}")
#Parcial 2
import re, requests
from collections import Counter

regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\"\s(\d{3})"

def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None

def ubicacion(ip):
    URI = "http://ip-api.com/json/"
    formatData = {}
    try:

        response = requests.get(f"{URI}{ip}").json()

        formatData["country"] = response.get("country")
        formatData["city"] = response.get("city")
    except Exception as e:
        formatData["country"] = None
        formatData["city"] = None
        print(f"Error al obtener la ubicación para {ip}: {e}")

    return formatData

ipsCode = []

for i in range(1, 6):
    ruta = f"C:\\Users\\306\\Downloads\\archive\\http\\access_log.{i}"

    try:
        with open(ruta, "rt") as file:
            for line in file:
                resultado = extractFromRegularExpresion(regex, line)

                if resultado:
                    ipsCode.extend(resultado)

    except FileNotFoundError:
        print(f"El archivo {ruta} no se encontró.")


contadorIps = Counter(ipsCode)


for (ip, error_code), count in contadorIps.items():
    location = ubicacion(ip)
    print(f"IP: {ip} // Código de error: {error_code} // País: {location['country']} // Ciudad: {location['city']} // Cantidad: {count}")

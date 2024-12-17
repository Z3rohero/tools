import phonenumbers
from phonenumbers import geocoder,carrier,timezone
import folium
from geopy.geocoders import Photon

def obtener_info_telefono(numero_telefono):
    """Obtener datos de geolocalizacion de un numero de telefono"""
    numero = phonenumbers.parse(numero_telefono)

    #Obtener la zona horaria
    zona_horaria = timezone.time_zones_for_number(numero)
    #Obtener el pais / region

    pais = geocoder.description_for_number(numero, "es")
    #Obtener el operador asociado con el numero
    operador = carrier.name_for_number(numero, "es")

    info = {
        "Numero": phonenumbers.format_number(numero,phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        "Pais":pais,
        "Operador":operador,
        "Zona horaira": zona_horaria
    }
    return info

def draw_map(localizacion,filename="phone_map.html"):
    """Construye un mapa con la localizacion de un numero de telefono"""
    geolocator = Photon(user_agent="geoapiExercise",timeout=10)
    location = geolocator.geocode(localizacion)
    mapa = folium.Map(locastion=[location.latitude , location.longitude],zoom_start=10)
    folium.Marker([location.latitude, location.longitude],popup=localizacion).add_to(mapa)

    #Guarda el mapa como un archivo html
    mapa.save(filename)
    print(f"El mapa guardo en: {filename}")

if __name__ =="__main__":
    #Ejemplo de uso
    numero = ""
    info = obtener_info_telefono(numero)
    for key,value in info.items():
        print(f" {key} : {value} ")

    draw_map(info["Pais"])


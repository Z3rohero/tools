import ipinfo
from dotenv import load_dotenv
import os 
import folium
#Configuracion
load_dotenv()
ACCESS_TOKEN = os.getenv("ACESS_TOKEN")
IP_ADDR = ""

def  draw_map(latitude,longitude,location, filename = "map.html"):
    """Dibuja un mapa basandonde en los detalles de geolocalizacion de una ip"""
    my_map = folium.Map(location=[latitude,longitude], zoom_start = 9)
    folium.Marker([latitude , longitude], popup=location).add_to(my_map)
    my_map.save(filename)
    return os.path.abspath(filename)

def  get_ip_details(ip_ddr,access_toke):
    """Obtiene detalles de geolocalizacion de una IP utilizando ipiinfo. """
    try:
        handler = ipinfo.getHandler(access_toke)
        details = handler.getDetails(ip_ddr)
        return details.all
    except Exception as e :
        print(f"Erro al obtner los detalles de la IP: {ip_ddr}")
        sys.exit(1)

if __name__ == "__main__":
    details = get_ip_details(IP_ADDR,ACCESS_TOKEN)
    #Mostramos los detalles de la ip por pantalla 
    for key,value in details.items():
        print(f"{key}: {value}")

    #Obtner los valores de latitud , longitud y localizacion
    latitude = details["latitude"]
    longitude = details["longitude"]
    location = details.get("region", "Ubicacion Desconocida")


    #Dibujar el mapa
    map_file_path = draw_map(latitude,longitude,location)
    print(f"Mapa guardado en: {map_file_path}")



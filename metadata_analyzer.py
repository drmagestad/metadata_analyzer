from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import piexif
import sys
import os
from geopy.geocoders import Nominatim

def get_image_metadata(imagename, output_file):
    """
    Función para extraer los metadatos de una imagen y guardarlos en un archivo de texto.
    """
    try:
        # Intentar abrir la imagen
        image = Image.open(imagename)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        sys.exit(1)

    # Extraer metadatos básicos
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    # Abrir el archivo de salida
    with open(output_file, "w") as file:
        # Guardar información básica en el archivo
        for label, value in info_dict.items():
            file.write(f"{label:25}: {value}\n")
        
        # Extraer los metadatos EXIF
        exifdata = image._getexif()
        if exifdata:
            file.write("\nEXIF Metadata:\n")
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)  # Obtener el nombre de la etiqueta EXIF
                data = exifdata.get(tag_id)    # Obtener el valor de la etiqueta
                
                # Si los datos son bytes, intentar decodificar
                if isinstance(data, bytes):
                    try:
                        data = data.decode('utf-8', errors='ignore')
                    except UnicodeDecodeError:
                        # Si no se puede decodificar, mostrar en hexadecimal
                        data = data.hex()
                
                # Procesar la información GPS si está presente
                if tag == "GPSInfo" and isinstance(data, dict):
                    gps_info = process_gps_info(data)
                    file.write(f"{tag:25}: {gps_info}\n")
                else:
                    # Escribir el valor EXIF
                    file.write(f"{tag:25}: {data}\n")
        else:
            file.write("\nNo EXIF data available.\n")

    print(f"Metadata saved to {output_file}")

def process_gps_info(gps_data):
    """
    Procesar la información GPS (latitud, longitud, etc.)
    """
    gps_info = {}
    
    # Verificar si existen datos GPS (latitud, longitud, etc.)
    if GPSTAGS.get(1) in gps_data:
        gps_info['Latitude'] = gps_data.get(GPSTAGS.get(2))  # GPSLatitude
        gps_info['Longitude'] = gps_data.get(GPSTAGS.get(4))  # GPSLongitude
        gps_info['Altitude'] = gps_data.get(GPSTAGS.get(6))   # GPSAltitude

    # Convertir de grados, minutos, segundos a grados decimales
    def convert_to_degrees(value):
        if isinstance(value, tuple) and len(value) == 3:
            degrees = value[0]
            minutes = value[1]
            seconds = value[2]
            return degrees + (minutes / 60.0) + (seconds / 3600.0)
        return None

    gps_info_decimals = {}
    if gps_info.get('Latitude'):
        gps_info_decimals['Latitude'] = convert_to_degrees(gps_info['Latitude'])
    if gps_info.get('Longitude'):
        gps_info_decimals['Longitude'] = convert_to_degrees(gps_info['Longitude'])

    # Preparar la cadena de GPS info para que sea legible
    gps_info_string = "\n".join([f"{key}: {value}" for key, value in gps_info_decimals.items()])
    
    if gps_info_string:
        # Si GPS está presente, usar Geopy para obtener la ubicación legible
        lat = gps_info_decimals.get('Latitude')
        lon = gps_info_decimals.get('Longitude')
        if lat and lon:
            geolocator = Nominatim(user_agent="metadata_analyzer")
            location = geolocator.reverse((lat, lon), language="es", timeout=10)
            gps_info_string += f"\nUbicación: {location.address if location else 'Desconocida'}"
    
    return gps_info_string if gps_info_string else "GPS data unavailable"

if __name__ == "__main__":
    # Solicitar la ruta de la imagen
    imagename = input("Introduce la ruta de la imagen (incluyendo la extensión, como 'image.jpg'): ")

    if not imagename or not os.path.exists(imagename):
        print("Por favor, proporciona una ruta válida para la imagen.")
        sys.exit(1)
    
    # Solicitar el nombre del archivo de salida (con extensión .txt)
    output_file = input("Introduce el nombre del archivo de salida (con extensión '.txt'): ")

    if not output_file.endswith(".txt"):
        print("El nombre del archivo de salida debe tener la extensión '.txt'.")
        sys.exit(1)
    
    # Llamar a la función principal para procesar la imagen
    get_image_metadata(imagename, output_file)

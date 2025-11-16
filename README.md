<h1 align="center">Metadata Analyzer</h1>

Este proyecto en Python permite extraer metadatos de imágenes, incluyendo información EXIF, GPS, software utilizado, y otros detalles. El script extrae la metadata de imágenes y la guarda en un archivo de texto legible.

## Características

- Extrae información básica de la imagen: tamaño, resolución, formato, etc.
- Extrae datos EXIF, como la fecha de creación, la cámara utilizada y el software.
- Extrae información GPS (si está disponible) y la convierte a coordenadas decimales.
- Utiliza `geopy` para obtener la ubicación legible a partir de las coordenadas GPS.
- Guarda todos los metadatos extraídos en un archivo de texto.

## Modo de uso

Para ejecutar este proyecto, necesitarás tener las siguientes librerías instaladas:

[Requirements](https://github.com/drmagestad/metadata_analyzer/blob/main/requirement.txt)

```bash
python metadata_analyzer.py
```

El script te pedirá que ingreses lo siguiente:

- Ruta de la imagen: La ruta completa o relativa del archivo de imagen que deseas analizar.
- Nombre del archivo de salida: El nombre del archivo .txt donde se guardarán los metadatos extraídos.

## Ejemplo de salida

<p align="center">
  <img src="https://github.com/drmagestad/metadata_analyzer/blob/main/img/resultado1.png" alt="INFO" />
</p>

<p align="center">
  <img src="https://github.com/drmagestad/metadata_analyzer/blob/main/img/resultado3.png" alt="INFO2" />
</p>

<h1 align="center">Metadata Analyzer</h1>

Este proyecto proporciona una forma sencilla de extraer metadatos de imágenes en formato JPG, JPEG y PNG. La clase `ImageMetadataExtractor` se encarga de extraer los metadatos EXIF de imágenes JPG y JPEG, y los metadatos generales de imágenes PNG.

## Funcionalidad

- **EXIF Metadata**: Para las imágenes en formato JPG y JPEG, se extraen los metadatos EXIF, como la orientación, fecha de creación, etc.
- **PNG Metadata**: Para imágenes PNG, se extraen los metadatos generales almacenados en `img.info`.
- **Soporte para múltiples formatos**: Actualmente soporta formatos JPG, JPEG y PNG.

## Instalación

### Requisitos previos

- Python 3.x
- La librería `Pillow` (una fork de `PIL`) es utilizada para abrir y procesar las imágenes.

Para instalar los requisitos, usa:

```bash
pip install Pillow

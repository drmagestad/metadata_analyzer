from metadata_analyzer import extract_metadata

if __name__ == "__main__":
    filepath = "/home/kali/Documents/Python hacking/seccion2/2_7_metadata_analyzer/Descargas/DSCN0010.jpg"
    metadata = extract_metadata(filepath)
    for key, value in metadata.items():
        print(f"{key}: {value}")

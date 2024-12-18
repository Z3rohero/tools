from metadata_analyzer import extract_metadata


if __name__ == "__main__":
    filepath = "/home/kali/Documentos/Desarrollo/tools/image/descargas/Canon_PowerShot_S40.jpg"
    metadata = extract_metadata(filepath)
    for key,value in metadata.items():
        print(f" {key} : {value}")
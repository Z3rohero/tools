from metadata_analyzer import extract_metadata


if __name__ == "__main__":
    #Colocar la ruta
    filepath = ""
    metadata = extract_metadata(filepath)
    for key,value in metadata.items():
        print(f" {key} : {value}")
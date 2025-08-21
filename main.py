# scripts/run_etl.py
from etl.extract import extract_data
from etl.transform import transform_data

def main():
    # Paso 1: extracción
    soup = extract_data()

    # Paso 2: transformación
    structured_data = transform_data(soup)

    # Por ahora mostramos parte de los datos transformados
    print("Items encontrados:", structured_data["total_items"])
    for item in structured_data["data"][:5]:  # solo los primeros 5
        print(item)

if __name__ == "__main__":
    main()

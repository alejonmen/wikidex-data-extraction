from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    """
    Limpia y normaliza cadenas de texto.
    """
    if not text:
        return ""
    return " ".join(text.split())  # quita espacios extra y saltos


def parse_elements(soup: BeautifulSoup) -> list[dict]:
    """
    Extrae información estructurada desde el objeto BeautifulSoup.
    Retorna una lista de diccionarios con los datos relevantes.
    """
    data = []

    # Ejemplo: extraer títulos y enlaces
    for idx, link in enumerate(soup.find_all("a", href=True), start=1):
        item = {
            "id": idx,
            "text": clean_text(link.get_text()),
            "url": link["href"]
        }
        data.append(item)

    return data


def transform_data(soup: BeautifulSoup) -> dict:
    """
    Orquesta el proceso de transformación:
    - Limpieza de texto
    - Estructuración en diccionarios
    Retorna un diccionario listo para exportar.
    """
    parsed = parse_elements(soup)
    return {
        "total_items": len(parsed),
        "data": parsed
    }

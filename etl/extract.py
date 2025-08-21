# etl/extract.py
import requests
from bs4 import BeautifulSoup
from config import settings


def extract_data():
    """
    Extrae datos desde la URL definida en settings.
    Retorna el objeto BeautifulSoup para procesamiento posterior.
    """
    response = requests.get(settings.TARGET_URL, headers=settings.REQUEST_HEADERS)
    response.raise_for_status()  # Lanza error si falla la petición

    soup = BeautifulSoup(response.text, "html.parser")
    return soup

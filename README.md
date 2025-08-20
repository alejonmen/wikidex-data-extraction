# Wikidex Data Extraction

## 🐍 Proyecto de Extracción de Datos con Python

### Objetivo
Proyecto de extracción de datos de Wikidex utilizando técnicas modernas de ETL (Extract, Transform, Load) con las siguientes tecnologías:

- 🌐 Web Scraping con BeautifulSoup
- 📦 Procesamiento de datos con Pandas
- 🔍 Extracción de información con Requests
- 📄 Exportación a formato JSON

### Características
- Extracción de información de Pokémon desde WikiDex
- Procesamiento y limpieza de datos
- Transformación estructurada
- Exportación para análisis posterior

### Tecnologías
- Python 3.8+
- BeautifulSoup4
- Pandas
- Requests
- JSON

### Disclaimer
Proyecto desarrollado con fines educativos y de práctica de técnicas de extracción de datos.


```
etl_project/
│
├── data/                       # Carpeta para almacenar datos en crudo y procesados
│   ├── raw/                    # Datos extraídos sin procesar
│   └── processed/              # Datos transformados/listos
│
├── etl/                        # Módulos principales del pipeline
│   ├── __init__.py
│   ├── extract.py              # Extracción de datos con requests + bs4
│   ├── transform.py            # Limpieza y transformación
│   ├── load.py                 # Exportar a JSON
│   └── utils.py                # Funciones auxiliares (logging, manejo de errores, etc.)
│
├── config/                     # Configuración del proyecto
│   ├── settings.py             # Config global (URLs, headers, paths de salida)
│   └── logging.conf            # Configuración de logs
│
├── tests/                      # Pruebas unitarias
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── notebooks/                  # Jupyter notebooks para pruebas rápidas (opcional)
│
├── scripts/                    # Scripts para ejecutar tareas
│   ├── run_etl.py              # Orquestación del pipeline completo
│   └── run_extract.py          # Ejecución puntual de la etapa de extracción
│
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Documentación inicial
└── .gitignore                  # Ignorar archivos innecesarios
```
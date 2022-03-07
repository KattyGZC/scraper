# scraper
Test backend developer

## Requerimientos
- pip
- python3
- venv

```
pip install virtualenv
```

## Instalación
```
python -m venv venv
./venv/Scripts/activate
(venv) pip install -r requirements.txt
```

## Intrucciones
1. Obtener el driver acorde a la versión de su navegador Chrome
- Si no tiene Chrome, descarguelo [aquí](https://www.google.com/intl/es/chrome/?brand=UUXU&gclsrc=ds&gclsrc=ds).
- Para saber la versión de su [Chrome](https://es.digitaltrends.com/computadoras/conocer-version-navegador/).
- Obtener [driver](https://chromedriver.chromium.org/downloads)
2. Descomprima el archivo .zip y obtenga el chromedriver.exe
3. Coloque el chromedriver.exe en la carpeta raiz del proyecto 
4. Ejecutar el siguiente comando, el cual descargará el archivo solicitado en formato .zip
```
(venv) python manage.py start_scraping
```
3. FInalizado el proceso anterior ejecutar el comando a continuación, este filtrara la información y la clasificará en distintos archivos .csv
```
(venv) python manage.py process_data <filename>.zip
```

## Para ejecutar los test unitarios
```
(venv) python -m unittest discover
```

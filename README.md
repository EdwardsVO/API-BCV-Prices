# API Tasa de Cambio Banco Central de Venezuela
Este proyecto proporciona una aplicación dockerizada que extrae las tasas de cambio del sitio web del Banco Central de Venezuela (BCV) y expone una API para acceder a estas tasas utilizando FastAPI.

## Características
1. Web Scraping: Extrae las tasas de cambio para varias monedas del sitio web del BCV.
2. Usabilidad: Utiliza la imagen directamente desde Docker Hub sin necesidad de clonar el repositorio.
3. FastAPI: Proporciona una API REST para acceder a las tasas de cambio extraídas.
4. Ligero: Construido sobre una imagen base de Python slim para mayor eficiencia.

## Cómo Usar
### Prerrequisitos
1. Docker instalado en tu sistema.
### Ejecutando la API
#### 1. Obtener la imagen de Docker:
`docker pull legrev/bcv-exchange-rates:latest`
#### 2. Ejecutar el contenedor de Docker:
`docker run -d -p 8000:8000 legrev/bcv-exchange-rates:latest`
#### 3. Acceder a la API
Abre tu navegador web y navega a `http://localhost:8000/get_exchange_rates` para ver las tasas de cambio.

## Ejemplo de Uso
Una vez que el contenedor esté en funcionamiento, puedes acceder a las tasas de cambio realizando una solicitud GET a:
- `http://localhost:8000/get_exchange_rates`
La API devolverá las tasas de cambio actuales extraídas del sitio web del BCV.

## Construyendo la Imagen desde el repositorio
Para construir la imagen localmente, sigue los siguientes pasos:
#### 1. Clonar el repositorio:
- `git clone https://github.com/EdwardsVO/API-BCV-Prices`
- `cd API-BCV-Prices`
#### 2. Construir la imagen de Docker:
`docker build -t bcv-exchange-rates .`
#### 3. Correr la imagen de forma local:
`docker run -d -p 8000:8000 --name bcv-exchange-rates-container bcv-exchange-rates`

## Contribuyendo
Las contribuciones son bienvenidas!!! Si tienes alguna mejora o sugerencia, no dudes en crear un pull request o abrir un issue. Juntos, podemos hacer este proyecto mejor para todos.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

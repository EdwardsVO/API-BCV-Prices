from fastapi import FastAPI
from .scraper.py import get_bcv_exchange_rates

app = FastAPI()

@app.get("/get_exchange_rates")
def get_exchange_rates():
    return get_bcv_exchange_rates()

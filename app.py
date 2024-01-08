from fastapi import FastAPI

from models import Currency, NBUCurrency
from storage_mongodb import storage

app = FastAPI()


@app.get("/check")
async def check():
    return {"status": "ok"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000
                )


@app.post("/currency/")
async def receive_currency(data: Currency) -> Currency:
    storage.add_currency(data)
    return data


@app.post("/nbu/")
async def store_nbu_data(nbu_currency: NBUCurrency):
    storage.add_nbu_currency(nbu_currency)
    return nbu_currency

from datetime import date

from fastapi import FastAPI, Request, Query

from models import Currency, NBUCurrency, ResponseInfo
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
async def receive_currency(data: Currency, request: Request) -> Currency:
    if request.client:
        data.user_ip = request.client.host
    else:
        data.user_ip = None
    storage.add_currency(data)

    return data


@app.post("/nbu/")
async def store_nbu_data(nbu_currency: NBUCurrency):
    storage.add_nbu_currency(nbu_currency)


@app.get("/currency/{exchange_date}")
async def get_currency_info(exchange_date: date, currency_name: str = Query('USD')) -> ResponseInfo:
    response_nbu = storage.get_nbu_info(currency_name, exchange_date)
    user_info = storage.get_user_info(currency_name, exchange_date)
    average_rate = 0
    if user_info:
        rates = [item.rate for item in user_info]
        average_rate = sum(rates) / len(rates)
    result = ResponseInfo(average=average_rate, response_nbu=response_nbu, user_info=user_info)
    return result

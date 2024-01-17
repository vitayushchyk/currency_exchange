from datetime import datetime

import requests

URL_DATA = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
URL_TO_SEND_DATA = 'http://127.0.0.1:8000/nbu/'


def fetch_and_send_currency_data():
    try:
        response = requests.get(URL_DATA)
        response.raise_for_status()

        data_from_nbu = response.json()

        for data in data_from_nbu:
            currency_data = {
                "digital_currency_code": data["r030"],
                "full_name_currency": data["txt"],
                "rate": data["rate"],
                "short_name_currency": data["cc"],
                "exchange_date": datetime.strptime(data["exchangedate"], "%d.%m.%Y").timestamp(),
            }

            response = requests.post(URL_TO_SEND_DATA, json=currency_data)
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Error fetching or sending data:", e)


if __name__ == '__main__':
    fetch_and_send_currency_data()

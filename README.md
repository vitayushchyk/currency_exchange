# currently_exchange

## components:

* data model
    * name
    * rate
    * exchange_date
    * user
    * user_ip
* updater periodically fetch data from common institution and store it in the system
* list of the endpoint:
    * `GET /currency/latest?currency_name={currency_name}`
    * `POST /currency/`
      ```json
      {
        "currency": "USD",
        "rate": 123,
        "date": "01-02-2024", 
        "user": "bob"
      }
      ```
    * `GET /check` return information is service is working or not

## tasks

* [x] create base simple web server with FastAPI:
  we can open the Swagger doc url and check, that it work
* [x] implement check endpoint
* [ ] take a coffe break :) with **Вафлями**
* [x] implement `POST /currency/` which will receive input model and return the same model to user.
  Need to just check, that endpoint works as expected.
* [x] Connect mongo DB to site, and store inside it, what user sent in the  `POST /currency/`
* [x] [Optional] catch user IP address and stor it to the database
* [x] write script, which will be started separately to fetch data about courses and insert it by
  call  `POST /currency/`
* [ ] extend `GET /currency/{date}?currency_name={currency_name}` to get information for given day
* [ ] extend `GET /currency/{date}?currency_name={currency_name}` to get with best course
* [ ] Copy conftest.py from teacher to me 
* [ ] Add test for each endpoint from app.py 

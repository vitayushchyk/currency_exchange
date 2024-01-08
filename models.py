from datetime import datetime

from pydantic import BaseModel


class Currency(BaseModel):
    currency: str
    rate: float
    date: datetime
    user: str
    institution: str
    user_ip: str


class NBUCurrency(BaseModel):
    digital_currency_code: float
    full_name_currency: str
    rate: float
    short_name_currency: str
    exchange_date: datetime

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Currency(BaseModel):
    short_name_currency: str
    rate: float
    exchange_date: datetime
    user_ip: Optional[str]


class NBUCurrency(BaseModel):
    digital_currency_code: float
    full_name_currency: str
    rate: float
    short_name_currency: str
    exchange_date: datetime


class ResponseInfo(BaseModel):
    average: float
    response_nbu: Optional[NBUCurrency]
    user_info: List[Currency]

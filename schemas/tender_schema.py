from pydantic import BaseModel
from typing import Optional, List


class FilterParams(BaseModel):
    type: Optional[List] = ["44-ФЗ\nЭлектронный аукцион", "223"]
    status: Optional[List] = ["Подача заявок", "Завершено"]



from pydantic import BaseModel
from typing import List, Optional

class PhonesIn(BaseModel):
    name: str
    model: str
    max_count: str
    operating: str


class PhonesOut(PhonesIn):
    id: int

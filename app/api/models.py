from pydantic import BaseModel
from typing import List, Optional

class PhoneIn(BaseModel):
    name: str
    model: str
    max_count: str
    operating: str


class PhoneOut(PhoneIn):
    id: int

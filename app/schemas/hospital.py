from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

Region = Literal["north", "northeast", "central", "east", "west", "south"]


# Lab 1.2 -------------------------------------------------------------
class HospitalCreate(BaseModel):
    """Input from client."""

    # TODO(1.2): add fields with validation rules
    #   name       str   length 3-200
    #   code       str   format like "BKK-001": 2-5 uppercase letters, dash, 3-5 digits
    #   region     Region
    #   bed_count  int   0 - 10,000
    #   is_active  bool  default True
    # Hint: Field(min_length=..., max_length=..., pattern=..., ge=..., le=...)
    ...


class HospitalOut(HospitalCreate):
    """Output to client."""

    # TODO(1.2): add fields the SERVER owns (client must never send these)
    # Question: why inherit from HospitalCreate instead of copying fields?
    ...

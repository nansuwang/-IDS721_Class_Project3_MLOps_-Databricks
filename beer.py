from pydantic import BaseModel


class beer(BaseModel):
    temp_median_c: float
    temp_min_c: float
    temp_max_c: float
    precip_mm: float
    beer_cons_liters: float

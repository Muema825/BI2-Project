from pydantic import BaseModel

class MentalForm(BaseModel):
    statement : str 
    
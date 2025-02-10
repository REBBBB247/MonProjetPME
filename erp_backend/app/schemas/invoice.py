from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    user_id: int
    total_amount: float

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

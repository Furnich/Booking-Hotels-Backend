



import pydantic
from sqlalchemy import Column, Float, Integer, String
from booking_hotels.database import Base


class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False,default="in progress")
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    description = Column(String, nullable=False)
    order_id = Column(String, nullable=False)
    invoice_id = Column(String, nullable=False)
    payment_type = Column(String, nullable=False)


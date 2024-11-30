from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from booking_hotels.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSONB)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    room = relationship("Rooms",back_populates="hotel")
    review = relationship("Reviews", back_populates="hotel")

    def __str__(self):
        return f"Отели {self.name} {self.location[:30]}"
    
class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'), nullable=False)
    user_id = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    hotel = relationship("Hotels", back_populates="review")
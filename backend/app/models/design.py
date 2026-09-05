from sqlalchemy import Column, Integer, Float, String

from app.database.database import Base


class Design(Base):
    __tablename__ = "designs"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String, nullable=False)
    material = Column(String, nullable=True)

    force_n = Column(Float, nullable=True)
    safety_factor = Column(Float, nullable=True)

    design_force_n = Column(Float, nullable=True)

    length_mm = Column(Float, nullable=True)
    width_mm = Column(Float, nullable=True)
    height_mm = Column(Float, nullable=True)
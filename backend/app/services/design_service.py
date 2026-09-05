from app.database.database import SessionLocal
from app.models.design import Design


def create_design(design_data: dict):
    db = SessionLocal()

    try:
        design = Design(**design_data)

        db.add(design)
        db.commit()
        db.refresh(design)

        return design

    finally:
        db.close()


def get_design(design_id: int):
    db = SessionLocal()

    try:
        return db.query(Design).filter(Design.id == design_id).first()

    finally:
        db.close()


def get_all_designs():
    db = SessionLocal()

    try:
        return db.query(Design).all()

    finally:
        db.close()
from sqlalchemy.orm import Session
import models, schemas


# Criminal CRUD operations
def create_criminal(db: Session, criminal: schemas.Criminal):
    db_criminal = models.Criminal(
        name=criminal.name,
        age=criminal.age,
        gender=criminal.gender,
        Fir_number=criminal.Fir_number
    )
    db.add(db_criminal)
    db.commit()
    db.refresh(db_criminal)
    return db_criminal


def get_criminal(db: Session, criminal_id: int):
    return db.query(models.Criminal).filter(models.Criminal.id == criminal_id).first()


def get_all_criminals(db: Session):
    return db.query(models.Criminal).all()


def update_criminal(db: Session, criminal_id: int, criminal: schemas.Criminal):
    db_criminal = db.query(models.Criminal).filter(models.Criminal.id == criminal_id).first()
    if db_criminal:
        db_criminal.name = criminal.name
        db_criminal.age = criminal.age
        db_criminal.gender = criminal.gender
        db_criminal.Fir_number = criminal.Fir_number
        db.commit()
        db.refresh(db_criminal)
    return db_criminal


def delete_criminal(db: Session, criminal_id: int):
    db_criminal = db.query(models.Criminal).filter(models.Criminal.id == criminal_id).first()
    if db_criminal:
        db.delete(db_criminal)
        db.commit()
    return db_criminal


# Police CRUD operations
def create_police(db: Session, police: schemas.Police):
    db_police = models.Police(
        name=police.name,
        age=police.age,
        gender=police.gender,
        role=police.role
    )
    db.add(db_police)
    db.commit()
    db.refresh(db_police)
    return db_police


def get_police(db: Session, police_id: int):
    return db.query(models.Police).filter(models.Police.id == police_id).first()


def get_all_police(db: Session):
    return db.query(models.Police).all()


def update_police(db: Session, police_id: int, police: schemas.Police):
    db_police = db.query(models.Police).filter(models.Police.id == police_id).first()
    if db_police:
        db_police.name = police.name
        db_police.age = police.age
        db_police.gender = police.gender
        db_police.role = police.role
        db.commit()
        db.refresh(db_police)
    return db_police


def delete_police(db: Session, police_id: int):
    db_police = db.query(models.Police).filter(models.Police.id == police_id).first()
    if db_police:
        db.delete(db_police)
        db.commit()
    return db_police
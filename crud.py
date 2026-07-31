from sqlalchemy.orm import Session
import models, schemas


# Criminal CRUD operations
def create_criminal(db: Session, criminal: schemas.Criminal_Register):
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


def update_criminal(db: Session, criminal: schemas.Criminal_Response):
    db_criminal = db.query(models.Criminal).filter(models.Criminal.id == criminal.id).first()
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
def create_police(db: Session, police: schemas.Police_Register):
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

#Lawyer CRUD operations
def create_lawyer(db:Session,lawyer:schemas.Lawyer_Register):
    db_lawyer=models.Lawyer(
        name=lawyer.name,
        age=lawyer.age,
        gender=lawyer.gender,
        role=lawyer.role
    )
    db.add(db_lawyer)
    db.commit()
    db.refresh(db_lawyer)
    return db_lawyer

def get_lawyer(db:Session,lawyer_id:int):
    return db.query(models.Lawyer).filter(models.Lawyer.id==lawyer_id).first()

def get_all_lawyers(db:Session):
    return db.query(models.Lawyer).all()

def update_lawyer(db:Session,lawyer_id:int,lawyer:schemas.Lawyer_Response):
    db_lawyer=db.query(models.Lawyer).filter(models.Lawyer.id==lawyer_id).first()
    if db_lawyer:
        db_lawyer.name=lawyer.name
        db_lawyer.age=lawyer.age
        db_lawyer.gender=lawyer.gender
        db_lawyer.role=lawyer.role
        db.commit()
        db.refresh(db_lawyer)
    return db_lawyer

def delete_lawyer(db:Session,lawyer_id:int):
    db_lawyer=db.query(models.Lawyer).filter(models.Lawyer.id==lawyer_id).first()
    if db_lawyer:
        db.delete(db_lawyer)
        db.commit()
    return db_lawyer

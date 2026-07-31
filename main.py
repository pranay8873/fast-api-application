from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Criminal Records API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criminal endpoints
@app.post("/criminals/")
def create_criminal(criminal: schemas.Criminal, db: Session = Depends(get_db)):
    db_criminal = crud.create_criminal(db=db, criminal=criminal)
    return "created successfully"


@app.get("/criminals/{criminal_id}", response_model=schemas.Criminal)
def get_criminal(criminal_id: int, db: Session = Depends(get_db)):
    db_criminal = crud.get_criminal(db=db, criminal_id=criminal_id)
    if db_criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    return db_criminal


@app.get("/criminals/", response_model=list[schemas.Criminal])
def get_all_criminals(db: Session = Depends(get_db)):
    return crud.get_all_criminals(db=db)


@app.put("/criminals/{criminal_id}", response_model=schemas.Criminal)
def update_criminal(criminal_id: int, criminal: schemas.Criminal, db: Session = Depends(get_db)):
    db_criminal = crud.update_criminal(db=db, criminal_id=criminal_id, criminal=criminal)
    if db_criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    return db_criminal


@app.delete("/criminals/{criminal_id}")
def delete_criminal(criminal_id: int, db: Session = Depends(get_db)):
    db_criminal = crud.delete_criminal(db=db, criminal_id=criminal_id)
    if db_criminal is None:
        raise HTTPException(status_code=404, detail="Criminal not found")
    return {"message": "Criminal deleted successfully"}


# Police endpoints
@app.post("/police/", response_model=schemas.Police)
def create_police(police: schemas.Police, db: Session = Depends(get_db)):
    db_police = crud.create_police(db=db, police=police)
    return db_police


@app.get("/police/{police_id}", response_model=schemas.Police)
def get_police(police_id: int, db: Session = Depends(get_db)):
    db_police = crud.get_police(db=db, police_id=police_id)
    if db_police is None:
        raise HTTPException(status_code=404, detail="Police not found")
    return db_police


@app.get("/police/", response_model=list[schemas.Police])
def get_all_police(db: Session = Depends(get_db)):
    return crud.get_all_police(db=db)


@app.put("/police/{police_id}", response_model=schemas.Police)
def update_police(police_id: int, police: schemas.Police, db: Session = Depends(get_db)):
    db_police = crud.update_police(db=db, police_id=police_id, police=police)
    if db_police is None:
        raise HTTPException(status_code=404, detail="Police not found")
    return db_police


@app.delete("/police/{police_id}")
def delete_police(police_id: int, db: Session = Depends(get_db)):
    db_police = crud.delete_police(db=db, police_id=police_id)
    if db_police is None:
        raise HTTPException(status_code=404, detail="Police not found")
    return {"message": "Police deleted successfully"}


@app.get("/")
def read_root():
    return {"message": "Criminal Records API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
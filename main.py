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
@app.post("/criminals/",response_model=schemas.Criminal)
def create_criminal(criminal: schemas.Criminal, db: Session = Depends(get_db)):
    db_criminal = crud.create_criminal(db=db, criminal=criminal)
    return db_criminal


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

@app.post("/lawyer/", response_model=schemas.Lawyer_Response)
def create_lawyer(lawyer:schemas.lawyer_Register,db:Session=Depends(get_db)):
    db_lawyer=crud.create_lawyer(db=db,lawyer=lawyer)
    return db_lawyer

@app.get("/lawyer/{lawyer_id}", response_model=schemas.Lawyer_Response)
def get_lawyer(lawyer_id: int, db: Session = Depends(get_db)):
    db_lawyer = crud.get_lawyer(db=db, lawyer_id=lawyer_id)
    if db_lawyer is None:
        raise HTTPException(status_code=404, detail="Lawyer not found")
    return db_lawyer

@app.get("/lawyer/", response_model=list[schemas.Lawyer_Response])
def get_all_lawyers(db: Session = Depends(get_db)):
    return crud.get_all_lawyers(db=db)

@app.put("/lawyer/{lawyer_id}", response_model=schemas.Lawyer_Response)
def update_lawyer(lawyer_id: int, lawyer: schemas.Lawyer_Response, db: Session = Depends(get_db)):
    db_lawyer = crud.update_lawyer(db=db, lawyer_id=lawyer_id, lawyer=lawyer)
    if db_lawyer is None:
        raise HTTPException(status_code=404, detail="Lawyer not found")
    return db_lawyer

@app.delete("/lawyer/{lawyer_id}")
def delete_lawyer(lawyer_id: int, db: Session = Depends(get_db)):
    db_lawyer = crud.delete_lawyer(db=db, lawyer_id=lawyer_id)
    if db_lawyer is None:
        raise HTTPException(status_code=404, detail="Lawyer not found")
    return {"message": "Lawyer deleted successfully"}

@app.post("/judge/", response_model=schemas.Judge_Response)
def create_judge(judge:schemas.Judge_Register,db:Session=Depends(get_db)):
    db_judge=crud.create_judge(db=db,judge=judge)
    return db_judge

@app.get("/judge/{judge_id}", response_model=schemas.Judge_Response)    
def get_judge(judge_id: int, db: Session = Depends(get_db)):
    db_judge = crud.get_judge(db=db, judge_id=judge_id)
    if db_judge is None:
        raise HTTPException(status_code=404, detail="Judge not found")
    return db_judge

@app.get("/judge/", response_model=list[schemas.Judge_Response])
def get_all_judges(db: Session = Depends(get_db)):
    return crud.get_all_judges(db=db)

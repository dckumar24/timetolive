from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/screen-time")
def update_screen_time(data: schemas.ScreenTimeRequest, db: Session = Depends(get_db)):
    crud.save_screen_time(db, data)
    return {"message": "Screen time saved"}

@app.get("/screen-time/{user_id}", response_model=list[schemas.ScreenTimeResponse])
def get_screen_time(user_id: str, db: Session = Depends(get_db)):
    entries = crud.get_screen_time_by_user(db, user_id)
    return [
        schemas.ScreenTimeResponse(
            user_id=entry.user_id,
            packageName=entry.package_name,
            totalTimeInForeground=entry.total_time_in_foreground
        )
        for entry in entries
    ]




@app.get("/screen-time/{user_id}/insights", response_model=schemas.UsageInsights)
def get_usage_insights(user_id: str, db: Session = Depends(get_db)):
    entries = crud.get_screen_time_by_user(db, user_id)

    total_ms = sum(e.total_time_in_foreground for e in entries)
    total_hours = round(total_ms / 1000 / 60 / 60, 2)

    top_apps = [
        schemas.AppUsageSummary(
            packageName=e.package_name,
            usage_minutes=round(e.total_time_in_foreground / 1000 / 60, 2)
        )
        for e in entries
    ]

    return schemas.UsageInsights(
        user_id=user_id,
        total_usage_hours=total_hours,
        top_apps=top_apps
    )
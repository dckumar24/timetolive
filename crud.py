from sqlalchemy.orm import Session
import models, schemas

def save_screen_time(db: Session, data: schemas.ScreenTimeRequest):
    for usage in data.usage_data:
        entry = models.ScreenTime(
            user_id=data.user_id,
            package_name=usage.packageName,
            total_time_in_foreground=usage.totalTimeInForeground
        )
        db.add(entry)
    db.commit()

def get_screen_time_by_user(db: Session, user_id: str):
    return db.query(models.ScreenTime).filter(models.ScreenTime.user_id == user_id).all()

from sqlalchemy import Column, Integer, String, BigInteger
from database import Base

class ScreenTime(Base):
    __tablename__ = "screen_time"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    package_name = Column(String)
    total_time_in_foreground = Column(BigInteger)

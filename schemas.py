from pydantic import BaseModel
from typing import List

class AppUsageSummary(BaseModel):
    packageName: str
    usage_minutes: float

class UsageInsights(BaseModel):
    user_id: str
    total_usage_hours: float
    top_apps: List[AppUsageSummary]


class AppUsage(BaseModel):
    packageName: str
    totalTimeInForeground: int

class ScreenTimeRequest(BaseModel):
    user_id: str
    usage_data: List[AppUsage]

class ScreenTimeResponse(AppUsage):
    user_id: str

from core.app import app
from study_record.routes import router as study_record_router

app.include_router(study_record_router, prefix="/study-records", tags=["study-record"])

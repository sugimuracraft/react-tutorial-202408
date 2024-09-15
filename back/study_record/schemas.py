from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic.fields import Field
from pydantic.types import UUID4


class StudyRecordSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created_at: datetime
    updated_at: datetime
    title: str
    time: int


class StudyRecordListSchema(BaseModel):
    total_count: int
    total_time: int
    study_records: List[StudyRecordSchema]


class StudyRecordCreationSchema(BaseModel):
    title: str = Field(min_length=1)
    time: int


class StudyRecordUpdationSchema(StudyRecordCreationSchema):
    pass

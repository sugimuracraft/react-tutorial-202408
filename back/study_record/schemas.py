from typing import List
from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic.types import UUID4


class StudyRecordSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    title: str
    time: int


class StudyRecordListSchema(BaseModel):
    total_count: int
    study_records: List[StudyRecordSchema]


class StudyRecordCreationSchema(BaseModel):
    title: str
    time: int


class StudyRecordUpdationSchema(StudyRecordCreationSchema):
    pass

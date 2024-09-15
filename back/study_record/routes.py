from typing import Annotated, cast

from fastapi import APIRouter, Depends, Query
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from core.database import get_db
from core.schemas import EmptySchema, ListQuerySchema
from study_record.crud import create_item, delete_item, get_item, get_list, update_item
from study_record.models import StudyRecord
from study_record.schemas import (
    StudyRecordCreationSchema,
    StudyRecordListSchema,
    StudyRecordSchema,
    StudyRecordUpdationSchema,
)
from study_record.validators import validate_id

router = APIRouter()


@router.post("/")
def register_study_record(
    data: StudyRecordCreationSchema,
    session: Session = Depends(get_db),
):
    study_record = create_item(session, data)
    return StudyRecordSchema.model_validate(study_record)


@router.get("/")
def list_study_record(
    c: Annotated[int | None, Query(description="The count of items in a page.")] = 25,
    p: Annotated[int | None, Query(description="The page of list.")] = 1,
    *,
    session: Session = Depends(get_db),
):
    query_params = ListQuerySchema(
        count=c,
        page=p,
    )
    total_count, total_time, study_records = get_list(session, query_params)
    return StudyRecordListSchema(
        total_count=total_count,
        total_time=total_time,
        study_records=study_records,
    )


@router.get("/{id}")
def retrieve_study_record(
    id: UUID4,
    session: Session = Depends(get_db),
):
    validate_id(session, id)
    study_record = cast(StudyRecord, get_item(session, id))
    return StudyRecordSchema.model_validate(study_record)


@router.put("/{id}")
def modify_study_record(
    id: UUID4,
    data: StudyRecordUpdationSchema,
    session: Session = Depends(get_db),
):
    validate_id(session, id)
    study_record = update_item(session, id, data)
    return StudyRecordSchema.model_validate(study_record)


@router.delete("/{id}")
def remove_study_record(
    id: UUID4,
    session: Session = Depends(get_db),
):
    validate_id(session, id)
    delete_item(session, id)
    return EmptySchema()

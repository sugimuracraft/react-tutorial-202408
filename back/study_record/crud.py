from typing import List, Tuple, cast


from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy.sql import asc

from core.exceptions import raise_http_404_not_found
from core.schemas import ListQuerySchema
from study_record.models import StudyRecord
from study_record.schemas import StudyRecordCreationSchema, StudyRecordUpdationSchema


def create_item(
    session: Session,
    data: StudyRecordCreationSchema,
) -> StudyRecord:
    params = {
        "title": data.title,
        "time": data.time,
    }
    study_record = StudyRecord(**params)
    session.add(study_record)
    
    session.commit()
    return study_record


def get_list(
    session: Session,
    query_params: ListQuerySchema
) -> Tuple[int, List[StudyRecord]]:
    ids_query = session.query(StudyRecord.id)
    ids = [item[0] for item in ids_query.all()]

    study_records = (
        session.query(StudyRecord)
        .order_by(asc(StudyRecord.created_at))
        .limit(query_params.count)
        .offset(query_params.count * (query_params.page - 1))
        .all()
    )

    return len(ids), study_records


def get_item(
    session: Session,
    id: UUID4,
) -> StudyRecord | None:
    study_record = (
        session.query(StudyRecord)
        .filter(StudyRecord.id == id)
        .first()
    )
    return study_record


def update_item(
    session: Session,
    id: UUID4,
    data: StudyRecordUpdationSchema,
) -> StudyRecord:
    study_record = cast(StudyRecord, get_item(session, id))
    study_record.title = data.title
    study_record.time = data.time

    session.commit()
    return study_record


def delete_item(
    session: Session,
    id: UUID4,
) -> None:
    study_record = cast(StudyRecord, get_item(session, id))
    session.delete(study_record)
    
    session.commit()

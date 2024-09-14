from pydantic.types import UUID4
from sqlalchemy.orm import Session

from core.exceptions import raise_http_404_not_found
from study_record.crud import get_item


def validate_id(
    session: Session,
    id: UUID4,
) -> None:
    study_record = get_item(session, id)
    if study_record is None:
        raise_http_404_not_found()

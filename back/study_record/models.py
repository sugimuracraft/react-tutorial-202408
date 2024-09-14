from sqlalchemy.orm import Mapped

from core.models import Base, CommonMixin


class StudyRecord(CommonMixin, Base):
    title: Mapped[str]
    time: Mapped[int]

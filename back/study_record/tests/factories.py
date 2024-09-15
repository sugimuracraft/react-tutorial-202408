from factory.declarations import Sequence
from factory.faker import Faker

from core.database import SessionLocal
from core.tests.factories import CommonFactory
from study_record.models import StudyRecord


class StudyRecordFactory(CommonFactory):
    title = Sequence(lambda n: "学習内容{}".format(n + 1))
    time = Faker("random_int", min=1, max=10)

    class Meta:
        model = StudyRecord
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session


class CommonFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True

    @classmethod
    def refresh_from_db(cls, instance, session: Session):
        """Renew from DB."""
        return (
            session.query(cls._meta.model)
            .filter(cls._meta.model.id == instance.id)
            .first()
        )

from datetime import datetime
from re import sub
from uuid import uuid4

from sqlalchemy.event import listens_for
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime, Uuid


class Base(DeclarativeBase):
    pass


class CommonMixin:
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )


# イベントリスナーを使って自動的に `updated_at` を更新する
@listens_for(CommonMixin, "before_update", propagate=True)
def update_timestamp(mapper, connection, target):
    target.updated_at = func.now()

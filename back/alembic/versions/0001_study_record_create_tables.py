"""create_tables

Revision ID: 0001_study_record
Revises: 
Create Date: 2024-09-14 02:15:06.542938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0001_study_record'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    study_record = op.create_table('study_record',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(
        study_record,
        [
            {
                "id": "209af90d-f68d-4488-ae1e-31ce79cb8d39",
                "created_at": "2024-08-30 01:00:00",
                "updated_at": "2024-08-30 01:00:00",
                "title": "勉強の記録1",
                "time": 1
            },
            {
                "id": "f24ae960-8c4c-4c4d-834b-132abcea1579",
                "created_at": "2024-08-30 01:00:00",
                "updated_at": "2024-08-30 01:00:00",
                "title": "勉強の記録2",
                "time": 3
            },
            {
                "id": "cf7bd3cf-8716-46e5-be23-0d1584e6c6c2",
                "created_at": "2024-08-30 01:00:00",
                "updated_at": "2024-08-30 01:00:00",
                "title": "勉強の記録3",
                "time": 5
            },
        ],
    )


def downgrade() -> None:
    op.drop_table('study_record')

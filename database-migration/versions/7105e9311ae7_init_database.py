"""init_database

Revision ID: 7105e9311ae7
Revises: 
Create Date: 2024-01-07 23:35:44.529169

"""
from typing import Sequence, Union
import uuid
from alembic import op
from sqlalchemy import Column, Integer, String,TIMESTAMP,func
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = '7105e9311ae7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        Column('id',Integer,primary_key=True, autoincrement=True),
        Column('uuid',UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True),
        Column('username',String(30),nullable=False,unique=True),
        Column('first_name',String(30),nullable=False),
        Column('last_name',String(30),nullable=False),
        Column('middle_name',String(30),nullable=True),
        Column('timestamp_created',TIMESTAMP(timezone=False),default=func.now()),
    )


def downgrade() -> None:
     op.drop_table('users')

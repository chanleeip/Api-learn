"""db_setup

Revision ID: 3bc60eb782d1
Revises: 
Create Date: 2024-01-08 19:12:35.431029

"""
from typing import Sequence, Union
import uuid
from alembic import op
from sqlalchemy import Column, Integer, String,TIMESTAMP,func,Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM


# revision identifiers, used by Alembic.
revision: str = '3bc60eb782d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    gender_types=ENUM('male','female','non_binary',name='gender_types')
    op.create_table(
        'users',
        Column('id',Integer,primary_key=True, autoincrement=True),
        Column('uuid',UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True),
        Column('username',String(30),nullable=False,unique=True),
        Column('first_name',String(30),nullable=False),
        Column('last_name',String(30),nullable=False),
        Column('middle_name',String(30),nullable=True),
        Column('timestamp_created',TIMESTAMP(timezone=False),default=func.now()),
        Column('gender',Enum('male','female','non_binary',name='gender_types'),nullable=True)
    )


def downgrade() -> None:
    op.drop_table('users')

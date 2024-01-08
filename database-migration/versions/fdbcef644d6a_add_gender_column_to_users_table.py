"""add gender column to users table

Revision ID: fdbcef644d6a
Revises: c0d0a1282e61
Create Date: 2024-01-08 12:13:56.113989

"""
from typing import Sequence, Union
from enum import Enum
from alembic import op
from sqlalchemy import Column,Enum
from sqlalchemy.dialects.postgresql import ENUM


# revision identifiers, used by Alembic.
revision: str = 'fdbcef644d6a'
down_revision: Union[str, None] = 'c0d0a1282e61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    gender_types=ENUM('male','female','non_binary',name='gender_types')
    gender_types.create(op.get_bind())
    op.add_column('users',Column('gender',Enum('male','female','non_binary',name='gender_types'),nullable=True))


def downgrade() -> None:
    op.drop_column('users','gender')

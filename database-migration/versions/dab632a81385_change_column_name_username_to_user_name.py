"""change column name username to user_name

Revision ID: dab632a81385
Revises: 7105e9311ae7
Create Date: 2024-01-08 00:36:45.003010

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import String,Column

# revision identifiers, used by Alembic.
revision: str = 'dab632a81385'
down_revision: Union[str, None] = '7105e9311ae7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users','username',new_column_name='user_name')


def downgrade() -> None:
    op.alter_column('users','user_name',new_column_name='username')

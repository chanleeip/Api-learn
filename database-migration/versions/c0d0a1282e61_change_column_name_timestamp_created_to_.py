"""change column name timestamp_created to date_created

Revision ID: c0d0a1282e61
Revises: dab632a81385
Create Date: 2024-01-08 00:45:17.302776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0d0a1282e61'
down_revision: Union[str, None] = 'dab632a81385'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users','timestamp_created',new_column_name='date_created')


def downgrade() -> None:
     op.alter_column('users','date_created',new_column_name='timestamp_created')

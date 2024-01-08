"""create_table tasks

Revision ID: 31cf8d3009f1
Revises: 3bc60eb782d1
Create Date: 2024-01-08 23:49:33.407230

"""
from typing import Sequence, Union
import uuid
from alembic import op
from sqlalchemy import Column, Integer, String,TIMESTAMP,func,Enum,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM


# revision identifiers, used by Alembic.
revision: str = '31cf8d3009f1'
down_revision: Union[str, None] = '3bc60eb782d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_types=ENUM('finished','not_finished',name='status_types')
    priority_types=ENUM('high_priority','low_priority','no_priority',name='priority_types')
    op.create_table(
        'tasks',
        Column('id',Integer,primary_key=True, autoincrement=True),
        Column('task_id',UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True),
        Column('username',String(30), ForeignKey('users.username'),nullable=False,unique=True),
        Column('username_id',String(30), ForeignKey('users.uuid'),nullable=False),
        Column('status',Enum('finished','not_finished',name='status_types'),nullable=True),
        Column('priority',Enum('high_priority','low_priority','no_priority',name='priority_types'),nullable=True),
        Column('task_description',String(60),nullable=False),
        Column('task_name',String(20),nullable=False),
        Column('attachments',String(30),nullable=True),
        Column('tags',String(30),nullable=True), 
        Column('due_date',String(30),nullable=True),     
        Column('timestamp_created',TIMESTAMP(timezone=False),default=func.now()),
    )


def downgrade() -> None:
    op.drop_table('tasks')

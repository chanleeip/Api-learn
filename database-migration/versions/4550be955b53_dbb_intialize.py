"""dbb_intialize

Revision ID: 4550be955b53
Revises: 
Create Date: 2024-01-09 10:09:29.885452

"""
from typing import Sequence, Union

import uuid
from alembic import op
from sqlalchemy import Column, Integer, String,TIMESTAMP,func,Enum,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ENUM



# revision identifiers, used by Alembic.
revision: str = '4550be955b53'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_types=ENUM('finished','not_finished',name='status_types')
    priority_types=ENUM('high_priority','low_priority','no_priority',name='priority_types')
    gender_types=ENUM('male','female','non_binary',name='gender_types')
    op.create_table(
        'users',
        Column('id',Integer,primary_key=True, autoincrement=True),
        Column('uuid',UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True,unique=True),
        Column('username',String(30),nullable=False,unique=True,primary_key=True),
        Column('first_name',String(30),nullable=False),
        Column('last_name',String(30),nullable=False),
        Column('middle_name',String(30),nullable=True),
        Column('timestamp_created',TIMESTAMP(timezone=False),default=func.now()),
        Column('gender',Enum('male','female','non_binary',name='gender_types'),nullable=True)
    )
    op.create_table(
        'tasks',
        Column('id',Integer,primary_key=True, autoincrement=True),
        Column('task_id',UUID(as_uuid=True),default=uuid.uuid4,autoincrement=False,primary_key=True),
        Column('username',String(30), ForeignKey('users.username'),nullable=False,unique=True),
        Column('username_id',UUID(as_uuid=True), ForeignKey('users.uuid'),nullable=False),
        Column('status',Enum('finished','not_finished',name='status_types'),nullable=True),
        Column('priority',Enum('high_priority','low_priority','no_priority',name='priority_types'),nullable=True),
        Column('task_description',String(60),nullable=False),
        Column('task_name',String(20),nullable=False),
        Column('attachments',String(30),nullable=True),
        Column('tags',String(30),nullable=True), 
        Column('due_date',String(30),nullable=True),     
        Column('timestamp_created',TIMESTAMP(timezone=True),default=func.now()),
    )

def downgrade() -> None:
    pass

"""enum status field

Revision ID: eafed6640d87
Revises: ff64d61f9bd2
Create Date: 2022-09-11 15:41:10.495162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eafed6640d87'
down_revision = 'ff64d61f9bd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_task_status', table_name='task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_task_status', 'task', ['status'], unique=False)
    # ### end Alembic commands ###

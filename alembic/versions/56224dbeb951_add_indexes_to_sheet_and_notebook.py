"""Add indexes to Sheet and Notebook

Revision ID: 56224dbeb951
Revises: 9ba894d60e05
Create Date: 2024-05-06 14:40:55.085418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56224dbeb951'
down_revision = '9ba894d60e05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_notebook_tyne_id'), 'notebook', ['tyne_id'], unique=False)
    op.create_index(op.f('ix_sheet_tyne_id'), 'sheet', ['tyne_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sheet_tyne_id'), table_name='sheet')
    op.drop_index(op.f('ix_notebook_tyne_id'), table_name='notebook')
    # ### end Alembic commands ###
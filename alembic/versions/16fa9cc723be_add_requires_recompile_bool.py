"""Add requires recompile bool

Revision ID: 16fa9cc723be
Revises: ab07bc6b324b
Create Date: 2023-04-11 16:17:27.953084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fa9cc723be'
down_revision = 'ab07bc6b324b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tyne', sa.Column('requires_recompile', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tyne', 'requires_recompile')
    # ### end Alembic commands ###
"""Add a tick flag

Revision ID: 28faa5056162
Revises: 5af8aaaf7423
Create Date: 2022-12-19 17:09:34.961325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28faa5056162'
down_revision = '5af8aaaf7423'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tyne', sa.Column('has_tick', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_tyne_has_tick'), 'tyne', ['has_tick'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tyne_has_tick'), table_name='tyne')
    op.drop_column('tyne', 'has_tick')
    # ### end Alembic commands ###

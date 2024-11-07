"""Attributes and last modified

Revision ID: 5b1f48fc808e
Revises: d6dd0a9e6b57
Create Date: 2022-02-21 15:48:32.630759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1f48fc808e'
down_revision = 'd6dd0a9e6b57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sheet', sa.Column('contents', sa.JSON(), nullable=True))
    op.add_column('sheet', sa.Column('attributes', sa.JSON(), nullable=True))
    op.add_column('tyne', sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tyne', 'last_modified')
    op.drop_column('sheet', 'attributes')
    op.drop_column('sheet', 'contents')
    # ### end Alembic commands ###
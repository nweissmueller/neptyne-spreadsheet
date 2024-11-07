"""Google user identifications

Revision ID: 81555406c529
Revises: bf749e7c4f30
Create Date: 2024-06-06 12:24:16.703802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81555406c529'
down_revision = 'bf749e7c4f30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('google_workspace_user', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('google_workspace_user', sa.Column('google_id', sa.Text(), nullable=True))
    op.add_column('google_workspace_user', sa.Column('domain', sa.Text(), nullable=True))
    op.create_index(op.f('ix_google_workspace_user_google_id'), 'google_workspace_user', ['google_id'], unique=True)
    op.create_index(op.f('ix_google_workspace_user_user_id'), 'google_workspace_user', ['user_id'], unique=False)
    op.create_foreign_key(None, 'google_workspace_user', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'google_workspace_user', type_='foreignkey')
    op.drop_index(op.f('ix_google_workspace_user_user_id'), table_name='google_workspace_user')
    op.drop_index(op.f('ix_google_workspace_user_google_id'), table_name='google_workspace_user')
    op.drop_column('google_workspace_user', 'domain')
    op.drop_column('google_workspace_user', 'google_id')
    op.drop_column('google_workspace_user', 'user_id')
    # ### end Alembic commands ###
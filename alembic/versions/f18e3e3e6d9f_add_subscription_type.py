"""Add subscription type

Revision ID: f18e3e3e6d9f
Revises: e5885f631be1
Create Date: 2023-05-02 17:03:57.872559

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'f18e3e3e6d9f'
down_revision = 'e5885f631be1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stripe_subscription', sa.Column('subscription_type', sa.Text, server_default='INDIVIDUAL_BASE', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stripe_subscription', 'subscription_type')
    # ### end Alembic commands ###
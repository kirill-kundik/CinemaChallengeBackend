"""Removed oauth table and flask dance integration

Revision ID: 6bc7d13aa575
Revises: 7624bed54ba3
Create Date: 2020-11-19 14:54:46.941200

"""

# revision identifiers, used by Alembic.
revision = '6bc7d13aa575'
down_revision = '7624bed54ba3'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flask_dance_oauth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('provider', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('token', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('provider_user_id', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.oid'], name='flask_dance_oauth_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='flask_dance_oauth_pkey'),
    sa.UniqueConstraint('provider_user_id', name='flask_dance_oauth_provider_user_id_key')
    )
    # ### end Alembic commands ###

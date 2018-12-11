"""Init. Crete user.

Revision ID: 01_user
Revises: 
Create Date: 2018-12-01 17:50:33.444808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01_user'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
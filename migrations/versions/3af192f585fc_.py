"""empty message

Revision ID: 3af192f585fc
Revises: 
Create Date: 2021-08-06 02:28:40.016979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af192f585fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###

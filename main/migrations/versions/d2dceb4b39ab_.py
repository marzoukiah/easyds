"""empty message

Revision ID: d2dceb4b39ab
Revises: 
Create Date: 2021-06-27 19:12:37.233773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2dceb4b39ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('job_title', sa.String(length=200), nullable=True),
    sa.Column('job_type', sa.String(length=200), nullable=True),
    sa.Column('job_description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_user')
    op.drop_table('job')
    # ### end Alembic commands ###

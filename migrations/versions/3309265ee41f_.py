"""empty message

Revision ID: 3309265ee41f
Revises: 
Create Date: 2020-03-13 19:05:03.600205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3309265ee41f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mensajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('message', sa.String(length=400), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mensajes')
    # ### end Alembic commands ###

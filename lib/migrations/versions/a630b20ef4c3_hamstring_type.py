"""hamstring type

Revision ID: a630b20ef4c3
Revises: f1184684fc41
Create Date: 2023-09-22 20:54:35.883466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a630b20ef4c3'
down_revision = 'f1184684fc41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hamgstrings', sa.Integer(), nullable=True))
        batch_op.drop_column('hangstrings')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hangstrings', sa.INTEGER(), nullable=True))
        batch_op.drop_column('hamgstrings')

    # ### end Alembic commands ###

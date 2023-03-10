"""empty message

Revision ID: 891d94a45fa9
Revises: 5b82d3878e8b
Create Date: 2023-01-26 19:00:29.828982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891d94a45fa9'
down_revision = '5b82d3878e8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('vehiculos_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('vehiculos_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

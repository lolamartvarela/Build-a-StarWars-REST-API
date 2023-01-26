"""empty message

Revision ID: 55889f80ecad
Revises: 891d94a45fa9
Create Date: 2023-01-26 19:27:03.830190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55889f80ecad'
down_revision = '891d94a45fa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('usuario_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('personajes_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('planetas_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('vehiculos_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.alter_column('vehiculos_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('planetas_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('personajes_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('usuario_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###

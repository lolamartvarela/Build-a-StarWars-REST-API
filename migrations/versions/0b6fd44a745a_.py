"""empty message

Revision ID: 0b6fd44a745a
Revises: 10f9fd7ba825
Create Date: 2023-01-26 15:22:27.116641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b6fd44a745a'
down_revision = '10f9fd7ba825'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('personajes_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('planetas_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('vehiculos_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'usuario', ['usuario_id'], ['id'])
        batch_op.create_foreign_key(None, 'planetas', ['planetas_id'], ['id'])
        batch_op.create_foreign_key(None, 'vehiculos', ['vehiculos_id'], ['id'])
        batch_op.create_foreign_key(None, 'personajes', ['personajes_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehiculos_id')
        batch_op.drop_column('planetas_id')
        batch_op.drop_column('personajes_id')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###

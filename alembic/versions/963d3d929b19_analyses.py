"""Add analyses and worker_results tables.

Revision ID: 963d3d929b19
Revises: ea55c632ae8d
Create Date: 2016-05-09 08:58:34.603632

"""

# revision identifiers, used by Alembic.
revision = '963d3d929b19'
down_revision = 'ea55c632ae8d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.create_table('analyses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('ecosystem', sa.Integer(), nullable=True),
                    sa.Column('package', sa.String(length=255), nullable=True),
                    sa.Column('version', sa.String(length=255), nullable=True),
                    sa.Column('access_count', sa.Integer(), nullable=True),
                    sa.Column('started_at', sa.DateTime(), nullable=True),
                    sa.Column('finished_at', sa.DateTime(), nullable=True),
                    sa.Column('analyses', postgresql.JSONB(), nullable=True),
                    sa.Column('subtasks', postgresql.JSONB(), nullable=True),
                    sa.Column('release', sa.String(length=255), nullable=True),
                    sa.Column('audit', postgresql.JSONB(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_table('worker_results',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('worker', sa.String(length=255), nullable=True),
                    sa.Column('analysis_id', sa.Integer(), nullable=True),
                    sa.Column('task_result', postgresql.JSONB(), nullable=True),
                    sa.ForeignKeyConstraint(['analysis_id'], ['analyses.id'], ),
                    sa.PrimaryKeyConstraint('id'))
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.drop_table('worker_results')
    op.drop_table('analyses')
    # end Alembic commands ###

"""Add indexes for columns used in WHERE, JOIN, and GROUP BY queries

Revision ID: a1b2c3d4e5f6
Revises: 66d566283326
Create Date: 2026-04-15 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '66d566283326'
branch_labels = None
depends_on = None


def upgrade():
    # Index on user_id: used in WHERE filter_by(user_id=...) in routes
    # for manage_request, predict, and delete_request endpoints
    op.create_index(op.f('ix_loan_request_user_id'), 'loan_request', ['user_id'], unique=False)

    # Index on created_at: maps to Application_Date used in
    # groupby/filtering in 'Solve the history problem.py'
    op.create_index(op.f('ix_loan_request_created_at'), 'loan_request', ['created_at'], unique=False)

    # Index on property_area: maps to Property_Area used in
    # pivot_table and cross_tab (GROUP BY) in 'Solve the history problem.py'
    op.create_index(op.f('ix_loan_request_property_area'), 'loan_request', ['property_area'], unique=False)

    # Index on prediction: maps to Loan_Status used in
    # aggregation queries in 'Solve the history problem.py'
    op.create_index(op.f('ix_loan_request_prediction'), 'loan_request', ['prediction'], unique=False)

    # Index on credit_history: used in analysis filtering
    # in 'Solve the history problem.py'
    op.create_index(op.f('ix_loan_request_credit_history'), 'loan_request', ['credit_history'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_loan_request_credit_history'), table_name='loan_request')
    op.drop_index(op.f('ix_loan_request_prediction'), table_name='loan_request')
    op.drop_index(op.f('ix_loan_request_property_area'), table_name='loan_request')
    op.drop_index(op.f('ix_loan_request_created_at'), table_name='loan_request')
    op.drop_index(op.f('ix_loan_request_user_id'), table_name='loan_request')

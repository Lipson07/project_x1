#! /usr/bin/env bash

# Let the DB start
python ./app/backend_pre_start.py

# Generate new migration file
alembic revision --autogenerate

# Run migrations (Apply the migration)
alembic upgrade head

# Create initial data in DB
python ./app/initial_data.py
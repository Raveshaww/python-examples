# Notes
- Create folder structure for Alembic with `alembic init migrations`
- Edit `alembic.ini` to use the correct database driver
- Edit `env.py`to reference your database models
- run migrations with `alembic revision --autogenerate -m "Create user model"`
    - You can actually render the generated commands into sql if you wanted
- Apply the migration with `alembic upgrade heads`
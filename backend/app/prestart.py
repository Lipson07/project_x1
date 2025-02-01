#/**
# Create data base migration
# **/
import subprocess
import sys

from alembic.config import Config
from alembic import command

from app.core.config import ROOT


alembic_cfg = Config(ROOT.parent / "alembic.ini")

subprocess.run([sys.executable, "./app/backend_pre_start.py"])
command.revision(alembic_cfg, "--autogenerate")  # Generate new migration file
command.upgrade(alembic_cfg, "head")
subprocess.run([sys.executable, "./app/initial_data.py"])

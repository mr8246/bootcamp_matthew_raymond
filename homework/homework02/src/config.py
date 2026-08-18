"""
config.py
Loads environment variables from a .env file and provides
helpers to safely retrieve them and locate project paths.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    """Loads environment variables from a .env file."""
    load_dotenv()
    print("Loaded .env (if present)")


def get_key(name: str, default=None):
    """Retrieves an environment variable by name."""
    return os.getenv(name, default)


PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
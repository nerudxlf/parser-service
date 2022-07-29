import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path: str = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

tablename: str = os.environ.get("tablename")
shopname: str = os.environ.get("shopname")
table_id: str = os.environ.get("table_id")
google_spreadsheets: str = os.environ.get("google_spreadsheets")
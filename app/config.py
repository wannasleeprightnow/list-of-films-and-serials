from os import getenv

from dotenv import load_dotenv

load_dotenv()

SQLITE_DB_FILE = getenv("SQLITE_DB_FILE")
KP_API_KEY = getenv("KP_API_KEY")
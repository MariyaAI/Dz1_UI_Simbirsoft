import os
from pathlib import Path

MANAGER_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
BASE_DIR = Path(__file__).resolve().parent.parent
API_BASE_URL = os.getenv("API_BASE_URL") or "http://localhost:8080"

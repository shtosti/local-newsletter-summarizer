import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Gmail / Google Cloud
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLOUD_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLOUD_CLIENT_SECRET")
GOOGLE_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
GMAIL_USER = os.getenv("GMAIL_USER")

# Gmail API settings
GMAIL_TOKEN_FILE = "token.json"
GOOGLE_CREDENTIALS_FILE = "credentials.json"
GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
EMAIL_QUERY = "category:updates"

# Obsidian paths
OBSIDIAN_DAILY = os.path.expanduser("~/Documents/The_Vault/Summaries/AI-newsletters/daily")
OBSIDIAN_WEEKLY = os.path.expanduser("~/Documents/The_Vault/Summaries/AI-newsletters/weekly")

# Ollama settings
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")

# Summary settings
SUMMARY_DAILY = True
SUMMARY_WEEKLY = True
BATCH_SIZE = 3
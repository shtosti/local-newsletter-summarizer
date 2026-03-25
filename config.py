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
# EMAIL_QUERY = "category:updates"
EMAIL_QUERY = ""

# Obsidian paths
OBSIDIAN_DAILY_AI = os.path.expanduser("~/Documents/The_Vault/Summaries/AI-newsletters/daily")
OBSIDIAN_WEEKLY_AI = os.path.expanduser("~/Documents/The_Vault/Summaries/AI-newsletters/weekly")
OBSIDIAN_PRIVATE_DAILY = os.path.expanduser("~/Documents/The_Vault/Summaries/personal-email/daily")
OBSIDIAN_PRIVATE_WEEKLY = os.path.expanduser("~/Documents/The_Vault/Summaries/personal-email/weekly")

# Ollama settings
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")

# Summary settings
SUMMARY_DAILY = True
SUMMARY_WEEKLY = False
BATCH_SIZE = 10

# Prompt template settings
PROMPTS_FILE = os.getenv("PROMPTS_FILE", "prompts/templates.json")
DAILY_PROMPT_KEY = os.getenv("DAILY_PROMPT_KEY", "daily_summary")
WEEKLY_PROMPT_KEY = os.getenv("WEEKLY_PROMPT_KEY", "weekly_summary")

# Config-driven summary runs. Each run can target different Gmail query,
# prompt template, output folder, and output filename tag.
SUMMARY_RUNS = [
	{
		"name": "newsletters_daily",
		"enabled": False,
		"query": "-category:primary",
		"max_results": 10,
		"batch_size": BATCH_SIZE,
		"date_mode": "daily",
		"prompt_key": "daily_summary_AI",
		"output_folder": OBSIDIAN_DAILY_AI,
		"file_tag": "newsletters_daily",
	},
	{
		"name": "personal_daily",
		"enabled": True,
		"query": "-category:updates -category:promotions -category:social -category:forums",
		"max_results": 10,
		"batch_size": BATCH_SIZE,
		"date_mode": "daily",
		"prompt_key": "daily_summary_personal",
		"output_folder": OBSIDIAN_PRIVATE_DAILY,
		"file_tag": "personal_daily",
	},
	{
		"name": "newsletters_weekly",
		"enabled": True,
		"query": "-category:primary",
		"max_results": 20,
		"batch_size": BATCH_SIZE,
		"date_mode": "weekly",
		"prompt_key": "weekly_summary_AI",
		"output_folder": OBSIDIAN_WEEKLY_AI,
		"file_tag": "newsletters_weekly",
	},
	{
		"name": "personal_weekly",
		"enabled": True,
		"query": "-category:updates -category:promotions -category:social -category:forums -category:primary",
		"max_results": 20,
		"batch_size": BATCH_SIZE,
		"date_mode": "weekly",
		"prompt_key": "weekly_summary_personal",
		"output_folder": OBSIDIAN_PRIVATE_WEEKLY,
		"file_tag": "personal_weekly",
	},
]
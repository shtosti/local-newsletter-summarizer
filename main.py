from email_client.gmail import GmailClient
from processors.cleaner import decode_body, clean_email_body
from summarizer.ollama_summarizer import OllamaSummarizer
from markdown.writer import save_markdown
from utils.helpers import today_str, week_str
from utils.prompt_loader import PromptManager
from config import (
    SUMMARY_DAILY,
    SUMMARY_WEEKLY,
    BATCH_SIZE,
    PROMPTS_FILE,
    DAILY_PROMPT_KEY,
    WEEKLY_PROMPT_KEY,
)

def main():
    print("[INFO] Starting email summarizer pipeline...")
    gmail = GmailClient()
    summarizer = OllamaSummarizer()
    prompt_manager = PromptManager(PROMPTS_FILE)

    emails = gmail.fetch_emails(max_results=50)
    print(f"[INFO] Fetched {len(emails)} emails.")

    cleaned_texts = [clean_email_body(decode_body(e['body'])) for e in emails]

    if SUMMARY_DAILY:
        print("[INFO] Generating daily summary...")
        daily_prompt = prompt_manager.get_prompt(
            DAILY_PROMPT_KEY,
            variables={"date": today_str(), "batch_size": BATCH_SIZE},
        )
        daily_summary = summarizer.summarize_general(cleaned_texts[:BATCH_SIZE], prompt=daily_prompt)
        save_markdown(today_str(), daily_summary, summary_type="daily")

    if SUMMARY_WEEKLY:
        print("[INFO] Generating weekly summary...")
        weekly_prompt = prompt_manager.get_prompt(
            WEEKLY_PROMPT_KEY,
            variables={"week_label": week_str(), "batch_size": BATCH_SIZE},
        )
        weekly_summary = summarizer.summarize_general(cleaned_texts, prompt=weekly_prompt)
        save_markdown(week_str(), weekly_summary, summary_type="weekly")

if __name__ == "__main__":
    main()
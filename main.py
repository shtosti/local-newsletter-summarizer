from email_client.gmail import GmailClient
from processors.cleaner import decode_body, clean_email_body
from summarizer.ollama_summarizer import OllamaSummarizer
from markdown.writer import save_markdown
from utils.helpers import today_str, week_str
from config import SUMMARY_DAILY, SUMMARY_WEEKLY, BATCH_SIZE

def main():
    print("[INFO] Starting email summarizer pipeline...")
    gmail = GmailClient()
    summarizer = OllamaSummarizer()

    emails = gmail.fetch_emails(max_results=50)
    print(f"[INFO] Fetched {len(emails)} emails.")

    cleaned_texts = [clean_email_body(decode_body(e['body'])) for e in emails]

    if SUMMARY_DAILY:
        print("[INFO] Generating daily summary...")
        daily_summary = summarizer.summarize(cleaned_texts[:BATCH_SIZE], prompt="Create a concise daily markdown summary:")
        save_markdown(today_str(), daily_summary, summary_type="daily")

    if SUMMARY_WEEKLY:
        print("[INFO] Generating weekly summary...")
        weekly_summary = summarizer.summarize(cleaned_texts, prompt="Create a concise weekly markdown summary:")
        save_markdown(week_str(), weekly_summary, summary_type="weekly")

if __name__ == "__main__":
    main()
from email_client.gmail import GmailClient
from processors.cleaner import decode_body, clean_email_body
from summarizer.ollama_summarizer import OllamaSummarizer
from markdown.writer import save_markdown
from utils.helpers import today_str, week_str
from utils.prompt_loader import PromptManager
from config import (
    PROMPTS_FILE,
    SUMMARY_RUNS,
)


def date_for_mode(date_mode):
    return today_str() if date_mode == "daily" else week_str()


def main():
    print("[INFO] Starting email summarizer pipeline...")
    gmail = GmailClient()
    summarizer = OllamaSummarizer()
    prompt_manager = PromptManager(PROMPTS_FILE)

    for run in SUMMARY_RUNS:
        if not run.get("enabled", False):
            continue

        name = run.get("name", "summary_run")
        query = run.get("query", "")
        max_results = int(run.get("max_results", 50))
        batch_size = int(run.get("batch_size", 0))
        date_mode = run.get("date_mode", "daily")
        prompt_key = run.get("prompt_key", "")
        output_folder = run.get("output_folder")
        file_tag = run.get("file_tag", name)

        print(f"[INFO] Running summary profile: {name}")
        emails = gmail.fetch_emails(max_results=max_results, query=query)
        print(f"[INFO] {name}: fetched {len(emails)} emails.")

        cleaned_texts = [clean_email_body(decode_body(e['body'])) for e in emails]
        if batch_size > 0:
            cleaned_texts = cleaned_texts[:batch_size]

        date_label = date_for_mode(date_mode)
        variables = {
            "date": today_str(),
            "week_label": week_str(),
            "batch_size": batch_size,
        }
        prompt = prompt_manager.get_prompt(prompt_key, variables=variables)
        summary_text = summarizer.summarize_general(cleaned_texts, prompt=prompt)

        save_markdown(
            date_label,
            summary_text,
            summary_type=name,
            folder=output_folder,
            file_tag=file_tag,
        )

if __name__ == "__main__":
    main()
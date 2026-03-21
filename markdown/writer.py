import os
from config import OBSIDIAN_DAILY_AI, OBSIDIAN_WEEKLY_AI

def save_markdown(date_str, summary_text, summary_type="daily", folder=None, file_tag=None):
    if folder is None:
        folder = OBSIDIAN_DAILY_AI if summary_type == "daily" else OBSIDIAN_WEEKLY_AI
    os.makedirs(folder, exist_ok=True)

    md_text = f"""---
date: {date_str}
type: {summary_type}
---

# {summary_type.capitalize()} Email Summary - {date_str}

{summary_text}
"""
    tag = file_tag or summary_type
    file_path = os.path.join(folder, f"{date_str}_{tag}_summary.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"[INFO] Saved {summary_type} summary to {file_path}")
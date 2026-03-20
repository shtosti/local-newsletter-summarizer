import os
from config import OBSIDIAN_DAILY, OBSIDIAN_WEEKLY

def save_markdown(date_str, summary_text, summary_type="daily"):
    folder = OBSIDIAN_DAILY if summary_type=="daily" else OBSIDIAN_WEEKLY
    os.makedirs(folder, exist_ok=True)

    md_text = f"""---
date: {date_str}
type: {summary_type}
---

# {summary_type.capitalize()} Email Summary - {date_str}

{summary_text}
"""
    file_path = os.path.join(folder, f"{date_str}_{summary_type}_summary.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"[INFO] Saved {summary_type} summary to {file_path}")
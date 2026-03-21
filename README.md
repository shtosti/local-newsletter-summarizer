# local-newsletter-summarizer
Desktop Ollama-powered app to fetch newsletters from Gmail inbox and create concise and structured summaries.

## Prompt configuration

Prompts are externalized in `prompts/templates.json`.

- Edit prompt text in the `prompts` object (for example `daily_summary` and `weekly_summary`).
- Keep shared global instructions in `shared_prefix`.
- Use placeholders like `{date}`, `{week_label}`, and `{batch_size}` inside templates.

Prompt selection is configured in `config.py`:

- `PROMPTS_FILE`
- `DAILY_PROMPT_KEY`
- `WEEKLY_PROMPT_KEY`

You can also override those using environment variables with the same names.

## Separate outputs by prompt type

Use `SUMMARY_RUNS` in `config.py` to route different prompt types to different folders/files.

Each run supports:

- `enabled`: turn run on/off
- `query`: Gmail search query (for example newsletters vs personal)
- `max_results`: how many emails to fetch
- `batch_size`: how many cleaned emails to summarize (`0` means all fetched)
- `date_mode`: `daily` or `weekly`
- `prompt_key`: key from `prompts/templates.json`
- `output_folder`: destination folder
- `file_tag`: custom filename tag

Current defaults include separate runs for:

- `newsletters_daily`
- `personal_daily`
- `newsletters_weekly`
- `personal_weekly`

This lets personal and newsletter summaries be saved into different folders without changing application code.

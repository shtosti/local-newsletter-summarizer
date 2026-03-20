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

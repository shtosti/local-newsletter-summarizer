from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from config import GMAIL_TOKEN_FILE, GMAIL_SCOPES, GOOGLE_CREDENTIALS_FILE, EMAIL_QUERY

class GmailClient:
    def __init__(self):
        self.creds = None
        token_path = Path(GMAIL_TOKEN_FILE)
        creds_path = Path(GOOGLE_CREDENTIALS_FILE)

        if token_path.exists():
            self.creds = Credentials.from_authorized_user_file(str(token_path), GMAIL_SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not creds_path.exists():
                    raise FileNotFoundError(f"Missing OAuth client file: {creds_path}")
                flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), GMAIL_SCOPES)
                self.creds = flow.run_local_server(port=0)

            token_path.write_text(self.creds.to_json(), encoding="utf-8")
        self.service = build('gmail', 'v1', credentials=self.creds)

    def fetch_emails(self, max_results=50):
        results = self.service.users().messages().list(userId='me', q=EMAIL_QUERY, maxResults=max_results).execute()
        messages = results.get('messages', [])
        return [self.get_email(msg['id']) for msg in messages]

    def get_email(self, msg_id):
        msg = self.service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        payload = msg['payload']
        headers = {h['name']: h['value'] for h in payload.get('headers', [])}
        body_data = payload.get('body', {}).get('data', '')
        return {
            "id": msg_id,
            "subject": headers.get("Subject", ""),
            "from": headers.get("From", ""),
            "date": headers.get("Date", ""),
            "body": body_data
        }
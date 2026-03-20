from bs4 import BeautifulSoup
import base64

def decode_body(body_data):
    return base64.urlsafe_b64decode(body_data).decode('utf-8')

def clean_email_body(body_html):
    soup = BeautifulSoup(body_html, 'html.parser')
    lines = [line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip()]
    return "\n".join(lines)
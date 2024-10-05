import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

params: resend.Emails.SendParams = {
    "from": "Test <testsendemail@resend.dev>",
    "to": ["dannychen170@gmail.com"],
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
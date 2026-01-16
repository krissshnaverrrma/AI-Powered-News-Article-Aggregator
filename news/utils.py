from django.conf import settings
from groq import Groq

from .models import Article


def fetch_and_summarize(headline_text, source_url):
    client = Groq(api_key=settings.GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an AI journalist specializing in the Indian tech ecosystem. "
                           "Summarize this Indian AI news headline in exactly 10 words."
            },
            {"role": "user", "content": headline_text}
        ],
    )
    summary = completion.choices[0].message.content
    Article.objects.create(title=headline_text,
                           link=source_url, summary=summary)

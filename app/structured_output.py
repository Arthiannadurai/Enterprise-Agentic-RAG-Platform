from google import genai
from google.genai import types
from pydantic import BaseModel
from enum import  Enum
from app.config import GEMINI_API_KEY, GEMINI_MODEL

class Priority(str, Enum):
    LOW =  "low"
    MEDIUM =  "Medium"
    HIGH =  "High"

class SupportTicket(BaseModel):
    category: str
    priority: Priority
    summary: str

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def classify_ticket(questions: str) -> SupportTicket | None :

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"""
        Classify the following support ticket.

        Ticket:
        {questions}

        Return JSON with exactly these fields:
        category
        priority
        summary
        """,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema= SupportTicket,
            temperature=0.2,
            max_output_tokens= 300
        )
    )

    return SupportTicket.model_validate_json(response.text)


if __name__ == "__main__":

    ticket = """
    I was charged twice for my subscription this month.
    Please refund the duplicate payment.
    """

    result = classify_ticket(ticket)

    print(result)
    print(result)
    print()
    print("Category:", result.category)
    print("Priority:", result.priority)
    print("Summary:", result.summary)
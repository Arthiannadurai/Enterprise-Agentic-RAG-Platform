from logging import exception
from google import genai
from app.config import GEMINI_API_KEY,GEMINI_MODEL
from google.genai import types
from app.logger import get_logger
from app.exceptions import LLMServiceError

logger = get_logger(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)
print(client)

def ask_llm(question: str) -> str | None:
    system_instruction = """
       You are an AI teacher. Explain technical concepts in simple language.
       with minimum line
       """
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents= question,
            config= types.GenerateContentConfig(
            # system_instruction = system_instruction,
            temperature =  0.9,
                # top_p=0.9,
                # max_output_tokens=2,
                # response_mime_type="application/json"

            )
        )
        if not response.text:
            raise LLMServiceError(
                "LLM returned an empty response."
            )
        return  response.text
    except LLMServiceError:
        raise
    except exception as exc:
     logger.exception("LLM request failed")
     raise LLMServiceError(
         "LLM service request failed."
     ) from exc

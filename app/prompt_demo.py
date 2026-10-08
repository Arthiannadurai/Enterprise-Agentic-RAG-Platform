
from google import genai

from google.genai import types
from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.prompts import Rag_system_prompt


client = genai.Client(
    api_key= GEMINI_API_KEY
)
def ask_teacher(question: str, contexts: str)->str | None:
    prompt = f"""
     Context:
     {contexts}
    
     Question:
     {question}
     """

    result = client.models.generate_content(
             model= GEMINI_MODEL,
             contents= prompt,
             config= types.GenerateContentConfig(
                 system_instruction= Rag_system_prompt,
                 temperature = 0.2,
                 max_output_tokens = 500
             )
        )
    return result.text


if __name__ == "__main__":
    context = """
        Embeddings are numerical vector representations of data.
        They represent the semantic meaning of text, images, or other data.
        Similar meanings are represented by vectors that are close to
        each other in the embedding space.
        """
    questionText = """
      Explain embeddings in AI.
      """
    answer = ask_teacher(questionText, context)
    print(answer)

from fastapi import FastAPI,status,HTTPException
from app.logger import get_logger
from app.llm import ask_llm
from app.config import APP_NAME,GEMINI_MODEL
from app.route.chat import router as chat_router
from app.document_loader import load_text_file



logger = get_logger(__name__)

app = FastAPI(title = "FastAPI",description = "Rag agent",version = "0.1.0")
app.include_router(chat_router)

@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return { "status": "ok"}



@app.get("/document/{documentId}")
def document(value: int):
    if value < 0:
        raise HTTPException(
            status_code= 404,
            detail="the document id not found"
        )
    return {"result": value}

@app.get("/search")
def search(query: str,top_k:int = 5):
    logger.info(
        "Search requested: query=%s top_k=%s",
        query,
        top_k
    )
    return {
        "query": query,
        "top_k": top_k
    }

@app.get ("test-error")
def test_error():
    try:
        result = 10/0
        return {"result": result}
    except Exception:
        logger.exception("unexpected error")
        raise HTTPException(status_code=500, detail="server error")

print("its working", __name__)
def main()->None:
    logger.info("Application starting")
    logger.info("Application name: %s", APP_NAME)
    logger.info("Configured model: %s", GEMINI_MODEL)
    logger.info("Project setup completed")
    question = "Give me 1 ideas for an AI Engineer project.?"
    answer = ask_llm(question)
    print("\nAI RESPONSE:")
    print(answer)

if __name__ == "__main__":
    main()
    # text = load_text_file("data/documents/employee_policy.txt")
    # print("data", text)

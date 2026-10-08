from app.schemas import ChangeRequest,ChangeResponse
from app.llm import ask_llm
from fastapi import APIRouter


router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)









@router.post("", response_model=ChangeResponse)
def chat(request: ChangeRequest):
    ans = ask_llm(request.message)
    return ChangeResponse(answer = ans)
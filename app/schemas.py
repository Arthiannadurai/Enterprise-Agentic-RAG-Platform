from pydantic import BaseModel, Field

class ChangeRequest(BaseModel):
    message: str = Field(min_length=1, max_length=200)

class ChangeResponse(BaseModel):
    answer: str | None
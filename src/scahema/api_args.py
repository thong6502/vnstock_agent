from typing import Optional
from pydantic import BaseModel, Field

class UserInput(BaseModel):
    input: str = Field(..., description="Câu hỏi hoặc yêu cầu của người dùng.")
    # language: Optional[str] = Field(None, description="Ngôn ngữ của đầu vào, ví dụ: 'vi', 'en'.")
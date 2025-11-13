from pydantic import BaseModel, Field
from typing import List, Dict, Any

class AgentSchema(BaseModel):
    answer: str = Field(..., description="Reponse from ai agent")
    tool_calls: List[Dict[str, Any]] = Field(
        ...,
        description="Danh sách lịch sử các lần AI agent gọi tool (gồm 3 trường thông tin lần lựt là name_tool, parameters và result)."
    )
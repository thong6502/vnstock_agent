from fastapi import FastAPI, Depends
app = FastAPI()

from src.agents.vnstock import run_agent_query
from src.schema.api import UserInput

@app.post("/vnstock")
def query_vnstock(user_input: UserInput):
    """
    Nhận truy vấn người dùng (input) và trả về phản hồi từ AI Agent.

    Args:
        user_input (UserInput): Dữ liệu đầu vào chứa câu hỏi người dùng.

    Returns:
        dict: 
            - `answer`: Nội dung trả lời của AI.
            - `tool_calls`: Danh sách các tool được gọi (nếu có).
    """
    response = run_agent_query(user_message=user_input.input)
    return {
        "answer": response.answer,
        "tool_calls": getattr(response, "tool_calls", None)
    }
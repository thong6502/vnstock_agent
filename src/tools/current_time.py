from langchain_core.tools import tool
from datetime import datetime

@tool()
def get_current_time() -> str:
    """Trả về ngày và giờ hiện tại dưới dạng chuỗi"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# current_time = get_current_time.func()
# print(current_time)
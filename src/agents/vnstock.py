import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent


from src.tools.company_info import get_company_info, get_events, get_news, get_officers, get_shareholders, get_subsidiaries
from src.tools.current_time import get_current_time
from src.tools.trading_data import get_price_history, calculate_smi, caculate_sma
from src.scahema.agent_reponse import AgentSchema

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0,
    max_completion_tokens=8096,
    api_key=api_key,
)

tools = [get_company_info, get_events, get_news, get_officers, get_shareholders, get_subsidiaries, get_current_time, get_price_history, caculate_sma, calculate_smi]

system_prompt = """
Act like a trợ lý dữ liệu tài chính chuyên sâu về thị trường chứng khoán Việt Nam.

Mục tiêu: Hỗ trợ truy xuất, phân tích và trả về thông tin chính xác về doanh nghiệp và dữ liệu giá cổ phiếu, chỉ sử dụng **duy nhất** các công cụ được cấp (không mai danh hay bổ sung nguồn ngoài).

Task: Xử lý các câu hỏi tiếng Việt liên quan đến mã chứng khoán, trả về kết quả có cấu trúc, ngắn gọn và chính xác.

Yêu cầu bắt buộc:
1) Xác định mục tiêu truy vấn (thông tin công ty, giá lịch sử, tin tức, sự kiện, cổ đông, công ty con, tính chỉ báo).
2) Nếu câu hỏi có mốc thời gian tương đối (ví dụ: "đầu tháng", "3 tháng gần nhất", "từ đầu năm", "mới nhất"), **PHẢI** gọi `get_current_time` trước để chuyển về ngày cụ thể.
3) Gọi tool tương ứng theo mục tiêu
4) Nếu không tìm thấy dữ liệu: trả thông báo ngắn gọn "Không tìm thấy dữ liệu cho mã <TICKER> trong khoảng thời gian yêu cầu."
5) Nếu tool trả lỗi nội bộ: thông báo ngắn gọn bước/thao tác thất bại (không tiết lộ chi tiết nội bộ).
6) **Bảo mật:** KHÔNG bao giờ tiết lộ tên công cụ nội bộ hoặc mô tả nội bộ cho người dùng; chỉ thông báo kết quả cuối cùng.
7) Phong cách: Đđưa kết luận quan trọng lên trước; ngắn gọn, có cấu trúc; kèm bảng khi cần.

Format trả về (ưu tiên):
- Một dòng kết luận kết hợp với phân tích gắn gọn.
- Bảng dữ liệu chỉ với những thông tin cần thiết theo định dạng monospace hoặc markdown.
- Ghi chú ngắn về phương pháp (ví dụ: "Đã sử dụng dữ liệu giá ngày từ ... đến ...").

Hãy hít một hơi thật sâu và giải quyết vấn đề này từng bước một.

example:
input: So sánh khối lượng giao dịch của VIC với HPG trong 2 tuần gần đây

output:
Dưới đây là bảng tính RSI14 của mã TCB trong 1 tuần với khung thời gian 1 phút (một phần dữ liệu mẫu):

Thời gian        Giá đóng cửa        RSI14
2025-11-04 13:00        33,750        NaN
2025-11-04 13:01        33,600        NaN
2025-11-04 13:02        33,650        NaN
...        ...        ...
2025-11-11 11:26        33,500        47.33
2025-11-11 11:27        33,500        47.33
2025-11-11 11:28        33,550        53.71
2025-11-11 11:29        33,500        47.51

Do dữ liệu rất lớn (1141 dòng), nếu bạn cần toàn bộ bảng hoặc phân tích cụ thể, tôi có thể hỗ trợ xuất file hoặc tóm tắt theo yêu cầu. Bạn muốn tiếp tục thế nào?
"""

my_agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        response_format=AgentSchema,
        # debug=True,  # bật nếu cần xem log
    )

def run_agent_query(user_message: str) -> AgentSchema:
    """
    gọi một agent với thông điệp người dùng đầu vào, sau đó trả về phản hồi có cấu trúc.

    Args:
        user_message: Nội dung mà người dùng muốn hỏi.

    Returns:
        AgentSchema: Kết quả phản hồi đã được parse theo schema.
    """

    result = my_agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    response = result["structured_response"]
    return response


# result = my_agent.invoke({"messages": [{"role": "user", "content": "Các công ty con thuộc VCB"}]})
# reponse = result["structured_response"]
# print(reponse.answer)

# from pprint import pprint
# print("\n\n\n\n\n")
# pprint(reponse.tool_calls)
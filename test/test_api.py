import requests

def test_vnstock_endpoint() -> None:
    """
    Unit test cho API endpoint /vnstock.
    """
    datas = [
        {"input": "Lấy dữ liệu OHLCV 10 ngày gần nhất HPG?"},
        {"input": "Lấy giá đóng cửa của mã VCB từ đầu tháng 11 theo khung 1d?"},
        {"input": "Trong các mã BID, TCB và VCB mã nào có giá mở cửa thấp nhất trong 10 ngày qua"},
        {"input": "Tổng khối lượng giao dịch (volume) của mã VIC trong vòng 1 tuần gần đây"},
        {"input": "So sánh khối lượng giao dịch của VIC với HPG trong 2 tuần gần đây"},
        {"input": "Danh sách cổ đông lớn của VCB"},
        {"input": "Danh sách ban lãnh đạo đang làm việc của VCB"},
        {"input": "Các công ty con thuộc VCB"},
        {"input": "Lấy cho tôi toàn bộ tên các lãnh đạo đang làm việc của VCB"},
        {"input": "Tính cho tôi SMA9 của mã VIC trong 2 tuần với timeframe 1d"},
        {"input": "Tính cho tôi RSI14 của TCB trong 1 tuần với timeframe 1m"},
        {"input": "Tính SMA9 và SMA20 của mã TCB từ đầu tháng 11 đến nay"},
    ]

    for data in datas:
        response = requests.post("http://localhost:8000/vnstock", json=data, timeout=100)
        content = response.json()  # gọi phương thức
        print("Question:", data["input"])
        print("Answer:", content.get("answer"))
        # print("Tool calls:", content.get("tool_calls"))
        print("-" * 50)

test_vnstock_endpoint()
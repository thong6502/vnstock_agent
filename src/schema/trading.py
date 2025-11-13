from pydantic import BaseModel, Field
from typing import Literal, Optional


class Symbol(BaseModel):
    symbol: str = Field(..., description="Mã chứng khoán (ticker), e.g, VCB")

class History(BaseModel):
    symbol: str = Field(..., description="Mã chứng khoán (ticker), ví dụ: VCB")
    start_date: str = Field(..., description="Ngày bắt đầu của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd")
    end_date: str = Field(..., description="Ngày kết thúc của truy vấn dữ liệu lịch sử. Định dạng YYYY-mm-dd")
    interval: Literal["1m", "5m", "15m", "30m", "1H", "1D", "1W", "1M"] = Field(
        "1D",
        description="Khung thời gian lấy mẫu dữ liệu."
    )
    window_size: int = Field(
        14,
        description="Kích thước cửa sổ tính toán, ví dụ 14"
    )

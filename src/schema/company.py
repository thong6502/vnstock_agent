from pydantic import BaseModel, Field
from typing import Literal


class Symbol(BaseModel):
    symbol: str = Field(..., description="Mã chứng khoán (ticker), ví dụ: VCB")


class Officers(BaseModel):
    symbol: str = Field(..., description="Mã chứng khoán (ticker), ví dụ: VCB")
    filter_officers: Literal["working", "resigned", "all"] = Field(
        "working",
        description="Trạng thái cán bộ cần lọc: 'working' (đang làm), 'resigned' (đã nghỉ), hoặc 'all' (tất cả)"
    )
from langchain_core.tools import tool
import pandas as pd
from vnstock import Company
from src.schema.company import Symbol, Officers


@tool(args_schema=Symbol)
def get_company_info(symbol: str) -> pd.DataFrame:
    """Lấy thông tin tổng quan doanh nghiệp"""
    company = Company(symbol=symbol, source='TCBS')
    return company.overview()


@tool(args_schema=Symbol)
def get_shareholders(symbol: str) -> pd.DataFrame:
    """Lấy thông tin cổ đông"""
    company = Company(symbol=symbol, source='TCBS')
    return company.shareholders()


@tool(args_schema=Officers)
def get_officers(symbol: str, filter_officers: str) -> pd.DataFrame:
    """Lấy thông tin ban lãnh đạo"""
    company = Company(symbol=symbol, source='TCBS')
    return company.officers(filter_by=filter_officers)


@tool(args_schema=Symbol)
def get_subsidiaries(symbol: str) -> pd.DataFrame:
    """Lấy thông tin công ty con"""
    company = Company(symbol=symbol, source='TCBS')
    return company.subsidiaries()


@tool(args_schema=Symbol)
def get_events(symbol: str) -> pd.DataFrame:
    """Lấy sự kiện doanh nghiệp"""
    company = Company(symbol=symbol, source='TCBS')
    return company.events()


@tool(args_schema=Symbol)
def get_news(symbol: str) -> pd.DataFrame:
    """Lấy tin tức doanh nghiệp"""
    company = Company(symbol=symbol, source='TCBS')
    return company.news()
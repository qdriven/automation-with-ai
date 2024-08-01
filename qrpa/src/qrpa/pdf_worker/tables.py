import pandas as pd
import tabula as tb


# Camelot 仅适用于基于文本的 PDF 文件，不适用于扫描的文档。
# 对于复杂的表格结构，可能需要手动调整参数或使用其他工具进行预处理。
def extract_table_data_simple(file_path: str, pages: str = "all", **kwargs) -> pd.DataFrame:
    """
    Extract Data from pdf file using camelot library:
    @param file_path: pdf file path
    @param pages: pages to extract
    @param kwargs: additional arguments for camelot.read_pdf
    """
    result = tb.read_pdf(file_path, pages=pages, **kwargs)
    return result


def convert_table_to_csv(file_path, output_path, pages="all"):
    tb.convert_into(file_path, output_path, pages)

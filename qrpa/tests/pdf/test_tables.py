import tabula
import pandas as pd


def extract_table_with_three_row_header(pdf_path, pages='all'):
    # Extract tables from the PDF
    tables = tabula.read_pdf(pdf_path, pages=pages, multiple_tables=True)

    processed_tables = []
    for table in tables:
        # Get the first three rows as headers
        header_row1 = table.columns
        header_row2 = table.iloc[0]
        header_row3 = table.iloc[1]

        # Combine the three header rows
        combined_header = []
        for col1, col2, col3 in zip(header_row1, header_row2, header_row3):
            combined = ' '.join(filter(lambda x: pd.notna(x) and x != '', [str(col1), str(col2), str(col3)]))
            combined_header.append(combined.strip())

        # Create a new DataFrame with the combined header
        new_table = pd.DataFrame(table.iloc[2:].values, columns=combined_header)

        # Clean up the data
        new_table = new_table.replace('', pd.NA).dropna(how='all').reset_index(drop=True)
        new_table = new_table.dropna(axis=1, how='all')

        processed_tables.append(new_table)
        tabula.convert_into(pdf_path, "output.csv", output_format="csv", pages="all")

    return processed_tables


def test_tabula_extract_table_data():
    result=extract_table_with_three_row_header("./foo.pdf")
    print(result)
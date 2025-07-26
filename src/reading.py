import csv
import pandas as pd


def reading_csv_file(csv_path):
    """Функция, которая читает данные из CSV-файла"""
    try:
        if csv_path:
            csv_data = pd.read_csv(csv_path)
            return csv_data.to_dict("records")
        else:
            return "Путь не найден"
    except Exception as e:
        return f"Поизошла ошибка {e}"


def reading_excel_file(excel_path):
    """Функция, которая читает данные из excel-файла"""
    try:
        if excel_path:
            excel_data = pd.read_excel(excel_path)
            return excel_data.to_dict("records")
        else:
            return "Путь не найден"
    except Exception as e:
        return f"Поизошла ошибка {e}"

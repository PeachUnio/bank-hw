from src.utils import load_transactions
from src.reading import reading_csv_file, reading_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.widget import mask_account_card, get_date

test_path = "C:/Users/Stealth/something/transactions_excel.xlsx"


def main(data_path):
    """
    Функция которая собирает основную логику программы банковского приложения и отдает список отфильтрованных функций
    для пользователя
    """
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        user_answer = input()
        if user_answer == "1":
            print("Для обработки выбран JSON-файл.")
            data_dict = load_transactions(data_path)
            break
        elif user_answer == "2":
            print("Для обработки выбран CSV-файла.")
            data_dict = reading_csv_file(data_path)
            break
        elif user_answer == "3":
            print("Для обработки выбран XLSX-файла")
            data_dict = reading_excel_file(data_path)
            break
        else:
            print("Для обработки выбран несуществующий вариант.")
            continue

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_answer_2 = input().upper()
        if user_answer_2 not in {"EXECUTED", "CANCELED", "PENDING"}:
            print(f"Статус операции {user_answer_2} недоступен.")
            continue
        else:
            filter_dict = filter_by_state(data_dict, user_answer_2)
            print(f"Операции отфильтрованы по статусу {user_answer_2}")
            break

    print("Отсортировать операции по дате? Да/Нет")
    user_answer_3 = input().lower()
    if user_answer_3 == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_answer_4 = input().lower()
        if user_answer_4 == "по возрастанию":
            filter_dict = sort_by_date(filter_dict, False)
        else:
            filter_dict = sort_by_date(filter_dict)

    print("Выводить только рублевые транзакции? Да/Нет")
    user_answer_5 = input().lower()
    if user_answer_5 == "да":
        filter_dict = [i for i in filter_dict
                       if i.get("currency_code", {}) == "RUB"]

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_answer_6 = input().lower()
    if user_answer_6 == "да":
        search_word = input("Введите слово для поиска: ")
        filter_dict = process_bank_search(filter_dict, search_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filter_dict)}")

    if filter_dict:
        for op in filter_dict:
            data = get_date(op["date"])
            description = op["description"]
            print(f"{data} {description}")

            if op["description"] == "Открытие вклада":
                id_1 = mask_account_card(op["to"])
                print(f"{id_1}")
            else:
                id_1 = mask_account_card(op["from"])
                id_2 = mask_account_card(op["to"])
                print(f"{id_1} -> {id_2}")

            if op["currency_code"] == "RUB":
                print(f"Сумма: {int(op["amount"])} руб.\n")
            else:
                print(f"Сумма: {int(op["amount"])} {op["currency_code"]}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")



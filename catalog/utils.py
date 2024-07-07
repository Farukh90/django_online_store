import json
import os.path


def create_contact_dict(name: str, phone: str, message: str) -> dict:
    contact_data = {"name": name, "phone": phone, "message": message}

    return contact_data


def read_JSON_data(file_path: str) -> list:
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except UnicodeDecodeError as e:
            print(f"ошибка {e}")
            with open(file_path, "r", encoding="windows-1251") as f:
                data = json.load(f)

    else:
        data = []
        print(f"файл {file_path} не существует")
    return data


def write_JSON_data(file_path: str, data) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

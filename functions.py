import json


def search(arg, path):
    """
    Данная функция выполняет поиск по файлу полученному JSON
    """
    dict_content = []
    with open(path, "r", encoding="utf-8") as file:
        post = json.load(file)

    for item in post:
        if arg in item["content"]:
            dict_content.append(item)
        else:
            continue
    return dict_content

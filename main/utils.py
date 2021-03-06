import json
from exceptions import *


def load_json_data(path):
    """Чтение JSON файла"""
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    """Поиск поста по подстроке"""
    post_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            post_founded.append(post)
    return post_founded

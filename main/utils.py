import json
from exception import *

def load_json_data(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    post_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            post_founded.append(post)
    return post_founded

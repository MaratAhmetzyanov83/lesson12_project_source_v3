import json

from config import UPLOAD_FOLDER, POST_PATH
from exceptions import WrongImgType


def save_picture(picture):
    """Функция сохраняет изображение в uploads/images"""
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType("Неверный формат файла")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path


def add_post(post_list, post):
    """Функция сохраняет пост"""
    post_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as file:
        json.dump(post_list, file)

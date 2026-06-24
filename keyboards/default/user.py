from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from data.config import WEB_APP_URL


def user_main_kb(url):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton(
            text="🛍 Mahsulotlar", web_app=WebAppInfo(
                url=url
            )
        )
    )
    return kb

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


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

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from data.config import APP_URL
from loader import dp, udb


@dp.message_handler(CommandStart(), state="*")
async def handle_start(message: types.Message, state: FSMContext):
    await state.finish()

    telegram_id = int(message.from_user.id)
    await udb.add_user(telegram_id)

    kb = types.InlineKeyboardMarkup()
    url = f"{APP_URL}/products/bot/"
    kb.add(
        types.InlineKeyboardButton(
            text="🛍 Mahsulotlar",
            web_app=types.WebAppInfo(
                url=url
            )
        )
    )


    await message.answer(
        text="Xush kelibsiz!",
        reply_markup=kb
    )

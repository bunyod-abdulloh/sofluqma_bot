from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from data.config import WEB_APP_URL
from keyboards.default.user import user_main_kb
from loader import dp, udb
from utils.tg_token import generate_tg_token


@dp.message_handler(CommandStart(), state="*")
async def handle_start(message: types.Message, state: FSMContext):
    await state.finish()

    telegram_id = int(message.from_user.id)
    await udb.add_user(telegram_id)

    token = generate_tg_token(message.from_user.id)
    url = f"{WEB_APP_URL}/products/bot/?tg_token={token}"

    await message.answer(
        text="Xush kelibsiz!",
        reply_markup=user_main_kb(url=url)
    )

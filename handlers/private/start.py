from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove
from magic_filter import F

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
            web_app=types.WebAppInfo(url=url)
        )
    )
    kb.add(
        types.InlineKeyboardButton(
            text="ℹ️ Qo'shimcha ma'lumot",
            callback_data="alert"
        )
    )

    text = (
        "🌿 <b>Assalomu alaykum! Sof Luqma sotuv botiga xush kelibsiz!</b> 🤝\n\n"

        "Bu yerda siz kimyoviy o'g'itlar va zararli zaharlardan xoli, "
        "tabiiy hamda ishonchli mahsulotlarni qulay tarzda buyurtma qilishingiz mumkin.\n\n"

        "🛒 <b>Bizning mahsulotlarimiz:</b>\n"
        "🍎 Ho'l mevalar\n"
        "🥜 Quruq mevalar\n"
        "🍉 Poliz ekinlari\n"
        "🌾 Dukkaklilar va donlar\n"
        "🌾 Un mahsulotlari\n"
        "🥩 Go'sht mahsulotlari\n"
        "🥛 Sut mahsulotlari\n"
        "🫒 Yog'lar\n"
        "🍶 Sirkalar\n"
        "🌿 Giyohlar\n"
        "🌱 Organik yorliqli mahsulotlar\n"
        "☕ Choy, qahva va boshqa ichimliklar\n"
        "🍯 Shinni va murabbolar\n"
        "🥟 Tayyor va yarim tayyor mahsulotlar\n"
        "🍬 Qand va shirinliklar\n\n"

        "💚 <b>Bizning maqsadimiz</b> — dasturxoningizga tabiiy, halol va sifatli mahsulotlarni yetkazib berish.\n\n"

        "👇 Quyidagi <b>🛍 Mahsulotlar</b> tugmasini bosing va xaridni boshlang.\n\n"

        "🌿 <b>Sof Luqma</b> — sog'lom turmush sari tabiiy tanlov!"
    )

    await message.answer(
        text=message.text,
        reply_markup=ReplyKeyboardRemove()
    )

    await message.answer(
        text=text,
        parse_mode="HTML",
        reply_markup=kb
    )


@dp.callback_query_handler(F.data == "alert")
async def h_alert(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer(
        text="Bu bo'limda qo'shimcha ma'lumotlar bo'ladi",
        show_alert=True
    )

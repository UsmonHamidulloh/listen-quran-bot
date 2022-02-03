from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    ans = f"<b>Ассаламу алайкум,</b> " + \
          f"<b><a href='tg://user?id={msg.from_user.id}'>{msg.from_user.full_name}</a>!</b>" + "\n\n"
    ans += "<b>Ботдан унумли фойдаланиш учун қуйидаги кўринишда хабар ёзинг:</b>" + "\n"
    ans += "{сура тартиб рақами}:{оят тартиб рақами}" + "\n\n"
    ans += "<b>Мисол учун бизга оятал курси керак бўлса (Бақара сураси, 255-оят), </b>" \
           "<b>ботга қуйидагича мурожаат қилишимиз керак:</b> <code>2:255</code>"

    await msg.answer(ans)

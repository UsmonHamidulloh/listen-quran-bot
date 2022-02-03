from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(msg: types.Message):
    ans = f"<b><a href='tg://user?id={msg.from_user.id}'>{msg.from_user.first_name}</a>,</b> " \
          f"<b>бот ишлашига бироз тушунмаган кўринасиз, келинг сизга ёрдам бераман.</b>" \
          + "\n\n"
    ans += "<b>Ботдан унумли фойдаланиш учун қуйидаги кўринишда хабар ёзинг:</b>" + "\n"
    ans += "{сура тартиб рақами}:{оят тартиб рақами}" + "\n\n"
    ans += "Мисол учун бизга оятал курси керак бўлса (Бақара сураси, 255-оят), " \
           "ботга қуйидагича мурожаат қилишимиз керак: "
    ans += "2:255"

    await msg.answer(ans)

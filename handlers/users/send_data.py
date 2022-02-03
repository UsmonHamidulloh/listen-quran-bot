from aiogram import types
from utils.alQuranCloud import get_sura_name
from utils.quranEnc import get_data
from loader import dp


@dp.message_handler()
async def send_data(msg: types.Message):
    if len(msg.text.split(':')) == 2:
        if get_data(msg.text):
            output = get_data(msg.text)
            output['surah_name'] = get_sura_name(msg.text)

            caption = (
                f"<b>«{output['surah_name']}» сураси, {output['number_in_surah']}-оят</b>",
                "<b>Alafasy қироати</b>"
            )

            ans = output['text'] + '\n\n'
            ans += f"<b>{output['translation']}</b>\n"
            ans += f"<a href='{output['image_url']}'> </a>\n"
            ans += f"«{output['surah_name']}» сураси, {output['number_in_surah']}-оят." + "\n\n"

            if output['footnotes'] != '':
                ans += output['footnotes'] + "\n\n"

            ans += "<b>— Алауддин Мансур тафсири</b>"

            await msg.answer_voice(output['audio'], "\n\n".join(caption))
            await msg.answer(ans)
        else:
            await msg.reply("<b>Маълумот топилмади.</b>")
    else:
        text = ("<b>Бот ишлатишда хатоликка йўл қойдингиз, илтимос тўғри сўров юборинг.</b>",
                "Агар ботни ишлатишга бироз тушунмаган бўлсангиз, /help ни босинг."
                )
        await msg.answer("\n\n".join(text))

from aiogram import types, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
        try:
            try:

                if send_audio(int(msg.text)):
                    name = get_sura_name(f'{int(msg.text)}:1')
                    await msg.answer_audio(
                        send_audio(int(msg.text)),
                        caption=f"<b>«{name}» сураси</b> | <b>Mishary Alafasy</b>"
                    )
                else:
                    ans = (
                        "<b>Қуръонда 114 сура мавжуд.</b>",
                        "Илтимос, 1 дан 114 гача бўлган сон киритинг"
                    )
                    await msg.reply('\n\n'.join(ans))
            except exceptions.WrongFileIdentifier:
                ans = (
                    "<b>Ботда хатолик юз берди, бу хатолик устида ҳозирда ишлаяпмиз</b>"
                    "<a href='https://telegra.ph/file/895a32ea912dd1409e82f.png'> </a>",
                    "Telegram-да bot орқали 50 МБ ҳажмдан кўп бўлган аудио жўнатса "
                    "<a href='https://core.telegram.org/bots/api#sendaudio'>бўлмас экан</a>. "
                    "Баъзи сураларнинг ҳажми 50 МБ-дан ошиб кетяпти, шу сабабдан хатолик юз беряпти. "
                    "Яқин орада бу хатоликка барҳам берамиз (биизниллаҳ).",
                    "<b>Ноқулайликлар учун узр сўраймиз..)</b>"
                )
                await msg.answer('\n\n'.join(ans), reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton('Админга мурожаат қилиш', url='https://t.me/h_toshkandiy')
                        ],
                        [
                            InlineKeyboardButton('Веб саҳифа', url='https://listen-quran.cf'),
                            InlineKeyboardButton('Telegram', url='https://t.me/ListenQuran_uz')
                        ]
                    ],
                ))
        except ValueError:
            text = ("<b>Бот ишлатишда хатоликка йўл қойдингиз, илтимос тўғри сўров юборинг</b>",
                    "Агар ботни ишлатишга бироз тушунмаган бўлсангиз, /help ни босинг."
                    )
            await msg.reply("\n\n".join(text))


def send_audio(num):
    if num < 10:
        return f'http://server8.mp3quran.net/afs/00{num}.mp3'
    elif num < 100:
        return f'http://server8.mp3quran.net/afs/0{num}.mp3'
    elif num <= 114:
        return f'http://server8.mp3quran.net/afs/{num}.mp3'
    else:
        return False

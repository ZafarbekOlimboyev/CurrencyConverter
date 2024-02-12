from hendlers.valyuta_changer_and_finder import other,kunlik,maxsus,convert_v
from aiogram import Router
from aiogram.types import Message

msg_co = Router()

@msg_co.message()
async def example(msg: Message):
    try:
        m = msg.text
        if m.count("-") == 2 and m.count(" ") == 1:
            msa = maxsus(m)
            await msg.reply(str(msa))
        elif m.count("-") == 2 and m.count(" ") == 0:
            ms = kunlik(m)
            await msg.reply(str(ms))
        elif m.isalpha():
            a = other(msg.text)
            await msg.reply(str(a))
        elif "-" not in m and m.count(" ") <= 1:
            f = convert_v(msg.text)
            await msg.reply(str(f))
    except:
        await msg.reply(f"<{msg.text}> nomalum narsa!!")
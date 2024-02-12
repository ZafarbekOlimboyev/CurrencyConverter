from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from hendlers.valyuta_changer_and_finder import kunlik, hafta
cmd_co = Router()
from main import Bot

@cmd_co.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer(text=f"Assalomu Alaykum {msg.from_user.full_name}! \t \nBotimizni qanday ishlatishni bilmasangiz /help buyrug'ini bosing.")

@cmd_co.message(Command("help"))
async def cmd_help(msg: Message):
    word = "Bizing bo'timzda quyidagi buyruqlar mavjud :\n\n\t/start - Botni qayta ishga tushurish\n\t/help - Botni ishlatish bo'yicha yo'riqnoma\n\t/kurs - Valyuta kursini bilish \n\t/hafta - Oxirgi haftada valyuta kursi\n\nAgar botimizdan ma'lum bir valyutani uzbek so'miga o'tkazmoqchi bo'lsangiz\n\tMasalan: 100 USD \nAgar ma'lum bir sanadagi valyutalar kursini bilmoqchi bo'lsangiz\n\tMasalan : 2024-01-17\nAgar ma'lum bir sanadagi ma'lum bir valyuta kursini bilmoqchi bo'lsangiz\n\t Masalan: 2024-01-17 USD\n\nIltimos botni ishlatganda yuqorida ko'rsatilganlarga amal qiling aks holda botda nosozliklar kuzatilishi mumkun!"
    await msg.reply(word)
@cmd_co.message(Command("kurs"))
async def cmd_kurs(msg: Message):
    m = kunlik()
    await msg.reply(str(m))
@cmd_co.message(Command("hafta"))
async def cmd_hafta(msg: Message):
    a = hafta()
    await msg.reply(str(a))

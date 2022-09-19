from concurrent.futures import Executor
import types
from aiogram import types ,executor, Dispatcher, Bot 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from unicodedata import name
import parzinh_hh 
import time
import schedule
import asyncio
import tracemalloc
tracemalloc.start(25)


TOK="5349032259:AAGxx9_kNinTUrYT_kCpcyBVBy95ReoGZcA"
bot = Bot(token=TOK)
dp=Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def begin(message:types.Message):
    kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    cnopka_start=types.KeyboardButton("Начать поиск")
    kap.add(cnopka_start)

    await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)

@dp.message_handler(content_types=["text"])

async def obshenie(message):
#    if message.text.lower()=="Пока":
#     await bot.send_message(message.chat.id, "Пользуйся пользовательским интерфейсом ввиде кнопок")
#     # await message.reply( "Пользуйся пользовательским интерфейсом ввиде кнопок")

    if message.text == "Начать поиск":
        den = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        finanze = types.KeyboardButton("Финансы и Экономика")
        urizt = types.KeyboardButton("Юриспруденция")
        Lin = types.KeyboardButton("Лингвистика")
        den.add(finanze, urizt, Lin)
        await bot.send_message(message.chat.id, "Какое твое направление обучения", reply_markup=den)
        

    if message.text == "Финансы и Экономика":
        # vigruzka(message)
        # for a in parzinh_hh.get_links("финансист+студент"):
        #     spisok=(parzinh_hh.get_resume(a))
        #     time.sleep(1)
        #     snils=str(spisok["Вакансия"])
        #     snils_one=str(spisok["Ссылка"])
        #     snils_TRY=str(spisok["Дата публикации"])
        #     await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
        # for a in parzinh_hh.get_links("экономист+студент"):
        #     spisok=(parzinh_hh.get_resume(a))
        #     time.sleep(1)
        #     snils=str(spisok["Вакансия"])
        #     snils_one=str(spisok["Ссылка"])
        #     snils_TRY=str(spisok["Дата публикации"])
        #     await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
        
        
        for i in  spiski_economist:
            for a in parzinh_hh.get_links(i):
                spisok=(parzinh_hh.get_resume(a))
                time.sleep(1)
                snils=str(spisok["Вакансия"])
                snils_one=str(spisok["Ссылка"])
                snils_TRY=str(spisok["Дата публикации"]) 
                await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")
                  


            # vosvrat()
          
    if message.text == "Юриспруденция":
            for a in parzinh_hh.get_links("юрист+студент"):
                spisok=(parzinh_hh.get_resume(a))
                time.sleep(1)
                snils=str(spisok["Вакансия"])
                snils_one=str(spisok["Ссылка"])
                snils_TRY=str(spisok["Дата публикации"])
                await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
            for a in parzinh_hh.get_links("начинающий+юрист"):
                spisok=(parzinh_hh.get_resume(a))
                time.sleep(1)
                snils=str(spisok["Вакансия"])
                snils_one=str(spisok["Ссылка"])
                snils_TRY=str(spisok["Дата публикации"])
                await bot.send_message(message.chat.id, f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )

    if message.text == "Лингвистика":
        ghf = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        nem = types.KeyboardButton("Немецкий")
        fran = types.KeyboardButton("Францу́зский")
        ingl = types.KeyboardButton("Английский")
        china = types.KeyboardButton("Китайский")
        strt = types.KeyboardButton("/start")
        ghf.add(nem, fran, ingl,china,strt)
        await bot.send_message(message.chat.id, "Какое твой язык?", reply_markup=ghf)


    if message.text == "Немецкий":
         for i in  spiski_perovod_nem:
            for a in parzinh_hh.get_links(i):
                    spisok=(parzinh_hh.get_resume(a))
                    time.sleep(1)
                    snils=str(spisok["Вакансия"])
                    snils_one=str(spisok["Ссылка"])
                    snils_TRY=str(spisok["Дата публикации"]) 
                    await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")

    if message.text == "Английский":
        for i in  spiski_perovod_ingl:
            for a in parzinh_hh.get_links(i):
                    spisok=(parzinh_hh.get_resume(a))
                    time.sleep(1)
                    snils=str(spisok["Вакансия"])
                    snils_one=str(spisok["Ссылка"])
                    snils_TRY=str(spisok["Дата публикации"]) 
                    await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")

   
    if message.text == "Францу́зский":               
        for i in  spiski_perovod_fr:
                for a in parzinh_hh.get_links(i):
                        spisok=(parzinh_hh.get_resume(a))
                        time.sleep(1)
                        snils=str(spisok["Вакансия"])
                        snils_one=str(spisok["Ссылка"])
                        snils_TRY=str(spisok["Дата публикации"]) 
                        await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")
    if message.text == "Китайский":  
        for i in  spiski_perovod_china:
                for a in parzinh_hh.get_links(i):
                        spisok=(parzinh_hh.get_resume(a))
                        time.sleep(1)
                        snils=str(spisok["Вакансия"])
                        snils_one=str(spisok["Ссылка"])
                        snils_TRY=str(spisok["Дата публикации"]) 
                        await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")



spiski_economist={
"финансист+студент",
"экономист+студент"
}
spiski_perovod_ingl={
"переводчик+английский+студент",
"английский+студент",
"лингвисит+английский+студент"
}
spiski_perovod_nem={
"переводчик+немецкий+студент",
"немецкий+студент",
"лингвисит+немецкий+студент"
}
spiski_perovod_fr={
"переводчик+французский+студент",
"французский+студент",
"лингвисит+французкий+студент"
}
spiski_perovod_china={
"переводчик+китайский+студент",
"китайский+студент",
"лингвисит+китайский+студент"
}

    
       


        
     

executor.start_polling(dp)
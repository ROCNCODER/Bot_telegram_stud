from concurrent.futures import Executor
import types
from aiogram import types ,executor, Dispatcher, Bot 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from unicodedata import name
# import time
# import schedule
# import asyncio
# import tracemalloc
import pymysql
# import cryptography
# from istok import host_one , port_one ,user_one,password_one,database_one





try:
    connection = pymysql.connect(
        host="92.53.124.26",
        port=3306,
        user="gen_user",
        password="71alidi6z3",
        database="default_db"    
    )
    print('Заебись')

   

except Exception as ex:
    print(ex)
    
with connection.cursor() as cursor:
                    zaproz="SELECT * FROM `Vacansian_economics` "
                    cursor.execute(zaproz)
                    rows = cursor.fetchall()

                    zaproz="SELECT * FROM `Vacansian_urist` "
                    cursor.execute(zaproz)
                    urist = cursor.fetchall()

                    zaproz="SELECT * FROM `Vacansian_lengvih` WHERE Язык='Анг'"
                    cursor.execute(zaproz)
                    ing = cursor.fetchall()

                    zaproz="SELECT * FROM `Vacansian_lengvih` WHERE Язык='Китай'"
                    cursor.execute(zaproz)
                    chin = cursor.fetchall()

                    zaproz="SELECT * FROM `Vacansian_lengvih` WHERE Язык='Нем'"
                    cursor.execute(zaproz)
                    nem = cursor.fetchall()

                    zaproz="SELECT * FROM `Vacansian_lengvih` WHERE Язык='Фр'"
                    cursor.execute(zaproz)
                    Fr = cursor.fetchall()
                    
try:

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
   
        if message.text == "Начать поиск":
            den = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            finanze = types.KeyboardButton("Финансы и Экономика")
            urizt = types.KeyboardButton("Юриспруденция")
            Lin = types.KeyboardButton("Лингвистика")
            stat= types.KeyboardButton("Перезапуск бота")
            den.add(finanze, urizt, Lin, stat)
            await bot.send_message(message.chat.id, "Какое твое направление обучения", reply_markup=den)
        

        if message.text == "Перезапуск бота":
            await bot.send_message(message.chat.id, "/start")


            

        if message.text == "Финансы и Экономика":
        
            for row in rows:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )      

        if message.text == "Юриспруденция":
        
            for row in urist:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )  

        if message.text == "Лингвистика":
            ghf = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            nem = types.KeyboardButton("Немецкий")
            fran = types.KeyboardButton("Францу́зский")
            ingl = types.KeyboardButton("Английский")
            china = types.KeyboardButton("Китайский")
            strt = types.KeyboardButton("Перезапуск бота")
            ghf.add(nem, fran, ingl,china,strt)
            await bot.send_message(message.chat.id, "Какой твой язык?", reply_markup=ghf)


        if message.text == "Немецкий":
            for row in nem:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )     

        if message.text == "Францу́зский":
            for row in Fr:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )  

        if message.text == "Английский":   
              for row in ing:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )   

        if message.text == "Китайский":   
              for row in chin:
                        snils=str(row[1])
                        snils_one=str(row[2])
                        snils_TRY=str(row[3])
                        await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )              
        




        
finally:
        connection.close()    
            
        
        


            
        

executor.start_polling(dp)











































                # vosvrat()
            
        # if message.text == "Юриспруденция":
        #         for a in parzinh_hh.get_links("юрист+студент"):
        #             spisok=(parzinh_hh.get_resume(a))
        #             time.sleep(1)
        #             snils=str(spisok["Вакансия"])
        #             snils_one=str(spisok["Ссылка"])
        #             snils_TRY=str(spisok["Дата публикации"])
        #             await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
        #         for a in parzinh_hh.get_links("начинающий+юрист"):
        #             spisok=(parzinh_hh.get_resume(a))
        #             time.sleep(1)
        #             snils=str(spisok["Вакансия"])
        #             snils_one=str(spisok["Ссылка"])
        #             snils_TRY=str(spisok["Дата публикации"])
        #             await bot.send_message(message.chat.id, f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )

        # if message.text == "Лингвистика":
        #     


        # if message.text == "Немецкий":
        #      for i in  spiski_perovod_nem:
        #         for a in parzinh_hh.get_links(i):
        #                 spisok=(parzinh_hh.get_resume(a))
        #                 time.sleep(1)
        #                 snils=str(spisok["Вакансия"])
        #                 snils_one=str(spisok["Ссылка"])
        #                 snils_TRY=str(spisok["Дата публикации"]) 
        #                 await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")

        # if message.text == "Английский":
        #     for i in  spiski_perovod_ingl:
        #         for a in parzinh_hh.get_links(i):
        #                 spisok=(parzinh_hh.get_resume(a))
        #                 time.sleep(1)
        #                 snils=str(spisok["Вакансия"])
        #                 snils_one=str(spisok["Ссылка"])
        #                 snils_TRY=str(spisok["Дата публикации"]) 
        #                 await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")

    
        # if message.text == "Францу́зский":               
        #     for i in  spiski_perovod_fr:
        #             for a in parzinh_hh.get_links(i):
        #                     spisok=(parzinh_hh.get_resume(a))
        #                     time.sleep(1)
        #                     snils=str(spisok["Вакансия"])
        #                     snils_one=str(spisok["Ссылка"])
        #                     snils_TRY=str(spisok["Дата публикации"]) 
        #                     await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")
        # if message.text == "Китайский":  
        #     for i in  spiski_perovod_china:
        #             for a in parzinh_hh.get_links(i):
        #                     spisok=(parzinh_hh.get_resume(a))
        #                     time.sleep(1)
        #                     snils=str(spisok["Вакансия"])
        #                     snils_one=str(spisok["Ссылка"])
        #                     snils_TRY=str(spisok["Дата публикации"]) 
        #                     await bot.send_message(message.chat.id,  f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}")

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

            
            
from aiogram import types, Dispatcher 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import ChatMemberMember, ChatMemberAdministrator,ChatMemberOwner
from create_bot import dp , bot
from keyboards import client_k







# @dp.message_handler(commands=["start"])
async def bot_message(message: types.Message):
        kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        cnopka_start=types.KeyboardButton("Начать поиск")
        kap.add(cnopka_start)
        await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)

# @dp.message_handler(content_types=["text"])   
async def obshenie(message):       
        user_status = await bot.get_chat_member(chat_id="@prolet_te", user_id=message.from_user.id)
        
        if isinstance(user_status, ChatMemberMember) or isinstance(user_status, ChatMemberAdministrator) or isinstance(user_status, ChatMemberOwner):
                    if message.text == "Начать поиск" :
                        await bot.send_message(message.chat.id, "Сфера к которой относится ваша проффесия или направление обучения", reply_markup = client_k.nabor_sferi)

                    if message.text == "Перезапуск бота" or  message.text == "/start":                     
                        kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        cnopka_start=types.KeyboardButton("Начать поиск")
                        kap.add(cnopka_start)
                        await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)       
                       
                    if message.text == "Экономические профессии":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_eco)
               
                    if message.text == "IT профессии":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_it)          
                        
                    if message.text == "Медицинские профессии":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_med)          
                        
                    if message.text == "Технические\Инженерные/строительные профессии/ручной труд":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_inge)    
  
                    if message.text == "Научные профессии":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_sni)       

                    if message.text == "Творческие профессии":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_tvor)       

                    if message.text == "Профессии сервиса (обслуживания)":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_ob) 

                    if message.text == "Юридические, правоохранительные (МЧС, МВД)":
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=client_k.nabor_ur)      

                    if message.text == "Лингвистика":
                        ghf = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        # nem = types.KeyboardButton("Немецкий")
                        # fran = types.KeyboardButton("Францу́зский")
                        # ingl = types.KeyboardButton("Английский")
                        # china = types.KeyboardButton("Китайский")
                        strt = types.KeyboardButton("Перезапуск бота")
                        ghf.add(strt)
                        await bot.send_message(message.chat.id, "Времмено на добаботке", reply_markup=ghf)
                    # nem, fran, ingl,china,
        else:
                bt_silca_na_canal= InlineKeyboardMarkup()
                butt= types.InlineKeyboardButton(text="Подпишись",url="https://t.me/prolet_te")
                bt_silca_na_canal.add(butt)
                await bot.send_message(message.chat.id,"Привет для начала использования бота потребентся подписатся на наш канал",reply_markup=bt_silca_na_canal)
              
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler (bot_message,commands=["start"])
    dp.register_message_handler (obshenie ,content_types=["text"])

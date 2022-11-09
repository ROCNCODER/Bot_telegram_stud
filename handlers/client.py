from aiogram import types, Dispatcher 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import ChatMemberMember, ChatMemberAdministrator,ChatMemberOwner
from create_bot import dp , bot






# @dp.message_handler(commands=["start"])
async def bot_message(message: types.Message):
        kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        cnopka_start=types.KeyboardButton("Начать поиск")
        kap.add(cnopka_start)
        await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)

# @dp.message_handler(content_types=["text"])   
async def obshenie(message):       
        user_status = await bot.get_chat_member(chat_id="@prolet_te", user_id=message.from_user.id)
        async def otpravca_vacancii(k):
                        kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        cnopka_start=types.KeyboardButton("Начать поиск")
                        kap.add(cnopka_start)
                        await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)              

                       
                        for row in k:
                                    snils=str(row[1])
                                    snils_one=str(row[2])
                                    snils_TRY=str(row[3])
                                    await bot.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" ) 
                        
                                    
                                   
        if isinstance(user_status, ChatMemberMember) or isinstance(user_status, ChatMemberAdministrator) or isinstance(user_status, ChatMemberOwner):
                    
               

                # or message.text =="Страница 1" 
        
                    if message.text == "Начать поиск" :
                        nabor_opit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        stud = types.KeyboardButton("Студент(без опыта)")
                        opit = types.KeyboardButton("Работник с опытом")	
                        nabor_opit.add(stud,opit)
                        await bot.send_message(message.chat.id, "Ваш трудовой опыт ?", reply_markup = nabor_opit)


                    
                    async def sfeer():   
                        await bot.send_message(message.chat.id, "Сфера к которой относится ваша проффесия или направление обучения", reply_markup=nabor_sferi)
                        


                        
                    if message.text == "Студент(без опыта)":

                        await bot.send_message(message.chat.id, "Выбери свой город", reply_markup=nabor_sity)
                                         
                        
                    if message.text == "Работник с опытом":
                        await bot.send_message(message.chat.id, "На обсуждении функционала")
                        # flag_opit="opit"
                        # sfeer()
                    


                        # den = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        # finanze = types.KeyboardButton("Финансы и Экономика")
                        # urizt = types.KeyboardButton("Юриспруденция")
                        # Lin = types.KeyboardButton("Лингвистика")
                        # fik = types.KeyboardButton("Тренер,Фитнес")
                        # stat= types.KeyboardButton("Перезапуск бота")
                        # str_two = types.KeyboardButton("Страница 2")
                        # den.add(finanze, urizt, Lin, fik, str_two , stat)
                        # await bot.send_message(message.chat.id, "Какое твое направление обучения", reply_markup=den)
                    

                    if message.text == "Перезапуск бота" or  message.text == "/start":                     
                        kap =  ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        cnopka_start=types.KeyboardButton("Начать поиск")
                        kap.add(cnopka_start)
                        await bot.send_message(message.chat.id,"Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=kap)       
                       
                    # if message.text == "Страница 2":
                    #     den = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    #     finanze = types.KeyboardButton("Дизайн")
                    #     urizt = types.KeyboardButton("Инженер(Общие вакансии)")
                    #     Lin = types.KeyboardButton("бухгалтер")
                    #     fik = types.KeyboardButton("Менеджер")
                    #     prod = types.KeyboardButton("Программист")
                    #     stat= types.KeyboardButton("Перезапуск бота")
                    #     str_two = types.KeyboardButton("Страница 1")
                    #     den.add(finanze, urizt, Lin, stat, fik, prod, str_two)
                    #     await bot.send_message(message.chat.id, "Какое твое направление обучения", reply_markup=den)

                    
                    

                    if message.text == "Экономические профессии":
                        
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Аудитор")
                        prof_one = types.KeyboardButton("Аналитик")
                        prof_two = types.KeyboardButton("Брокер")
                        prof_tree = types.KeyboardButton("Екатеринбург")
                        prof_fr = types.KeyboardButton("Продавец")
                        prof_fi = types.KeyboardButton("Кредитный консультант")
                        prof_six = types.KeyboardButton("Маркетолог")
                        prof_sev = types.KeyboardButton("Страховой агент")
                        prof_ete = types.KeyboardButton("Торговый представитель")
                        prof_nine = types.KeyboardButton("Экономист")
                        prof_ten = types.KeyboardButton("Финансист")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)

                     
                         
                    if message.text == "IT профессии":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Администратор базы данных")
                        prof_one = types.KeyboardButton("Веб-интеграторT")
                        prof_two = types.KeyboardButton("Оператор ПК")
                        prof_tree = types.KeyboardButton("Веб-мастер")
                        prof_fr = types.KeyboardButton("Программист")
                        prof_fi = types.KeyboardButton("Кодер")
                        prof_six = types.KeyboardButton("Веб-программист")
                        prof_sev = types.KeyboardButton("Тестировщик")
                        prof_ete = types.KeyboardButton("Геймдизайнер")
                        prof_nine = types.KeyboardButton("Программист")
                        prof_ten = types.KeyboardButton("Системный администратор")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)          
                        
                    if message.text == "Медицинские профессии":
                    
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Акушер-гинеколог")
                        prof_one = types.KeyboardButton("Аллерголог")
                        prof_two = types.KeyboardButton("Венеролог")
                        prof_tree = types.KeyboardButton("Врач скорой медицинской помощи")
                        prof_fr = types.KeyboardButton("Гастроэнтеролог ")
                        prof_fi = types.KeyboardButton("Дерматолог")
                        prof_six = types.KeyboardButton("Диетолог")
                        prof_sev = types.KeyboardButton("Кардиолог")
                        prof_ete = types.KeyboardButton("Косметолог")
                        prof_nine = types.KeyboardButton("Нарколог")
                        prof_ten = types.KeyboardButton("Онколог")
                        prof_eleven = types.KeyboardButton("Ортодонт")
                        prof_twelw = types.KeyboardButton("Ортопед")
                        prof_trinadtcat = types.KeyboardButton("Офтальмолог")
                        prof_fotin = types.KeyboardButton("Пластический хирург")
                        prof_fiften = types.KeyboardButton("Проктолог")
                        prof_sixten = types.KeyboardButton("Психиатр")
                        prof_eleventen = types.KeyboardButton("Психотерапевт")
                        prof_twelwten = types.KeyboardButton("Рентгенолог")
                        prof_ninten = types.KeyboardButton("Терапевт")
                        prof_twentyone = types.KeyboardButton("Травматолог")
                        prof_twentytwo = types.KeyboardButton("Фармацевт")
                        prof_twentytree = types.KeyboardButton("Фельдшер")
                        prof_twentyfore = types.KeyboardButton("Хирург")
                        prof_twentyfive = types.KeyboardButton("Уролог")
                        prof_twentysix = types.KeyboardButton("Эндокринолог")
                        prof_twentysewen = types.KeyboardButton("Эпидемиолог")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten,prof_eleven,prof_twelw ,prof_trinadtcat ,prof_fotin ,prof_fiften ,prof_sixten ,prof_eleventen ,prof_twelwten ,prof_ninten ,prof_twentytwo ,prof_twentyone ,prof_twentytree ,prof_twentyfore ,prof_twentyfive ,prof_twentysix,prof_twentysewen )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)          
                        
                     

                    if message.text == "Технические\Инженерные/строительные профессии/ручной труд":
                        
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Автослесарь")
                        prof_one = types.KeyboardButton("Автоэлектрик")
                        prof_two = types.KeyboardButton("Инженер-конструктор")
                        prof_tree = types.KeyboardButton("Инженер-механик")
                        prof_fr = types.KeyboardButton("Инженер по Технике Безопасности")
                        prof_fi = types.KeyboardButton("Инженер-системотехник")
                        prof_six = types.KeyboardButton("Инженер-строитель")
                        prof_sev = types.KeyboardButton("Кабельщик")
                        prof_ete = types.KeyboardButton("Кровельщик")
                        prof_nine = types.KeyboardButton("Маляр")
                        prof_ten = types.KeyboardButton("Механик")
                        prof_eleven = types.KeyboardButton("Монтажник")
                        prof_twelw = types.KeyboardButton("Плотник")
                        prof_trinadtcat = types.KeyboardButton("Сантехник")
                        prof_fotin = types.KeyboardButton("Сборщик")
                        prof_fiften = types.KeyboardButton("Сварщик")
                        prof_sixten = types.KeyboardButton("Техник")
                        prof_eleventen = types.KeyboardButton("Токарь")
                        prof_twelwten = types.KeyboardButton("Швея")
                        prof_ninten = types.KeyboardButton("Штукатур")
                        prof_twentyone = types.KeyboardButton("Электрик")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten,prof_eleven,prof_twelw ,prof_trinadtcat ,prof_fotin ,prof_fiften ,prof_sixten ,prof_eleventen ,prof_twelwten ,prof_ninten )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)    
  

                    if message.text == "Научные профессии":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Философ")
                        prof_one = types.KeyboardButton("Физик")
                        prof_two = types.KeyboardButton("Биолог")
                        prof_tree = types.KeyboardButton("Футуролог")
                        prof_fr = types.KeyboardButton("Географ")
                        prof_fi = types.KeyboardButton("Геодезист")
                        prof_six = types.KeyboardButton("Зоолог")
                        prof_sev = types.KeyboardButton("Логик")
                        prof_ete = types.KeyboardButton("Эколог")
                        prof_nine = types.KeyboardButton("Математик")
                        prof_ten = types.KeyboardButton("Социолог")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)       

                       

                    if message.text == "Транспортные профессии":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Водитель")
                        prof_one = types.KeyboardButton("Диспетчер")
                        prof_two = types.KeyboardButton("Кондуктор")
                        prof_tree = types.KeyboardButton("Слесарь-механик")
                        prof_fr = types.KeyboardButton("Стрелочник")
                        prof_fi = types.KeyboardButton("Таксист")
                    
                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)       

                    
                    if message.text == "Творческие профессии":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Актёр")
                        prof_one = types.KeyboardButton("Балерина")
                        prof_two = types.KeyboardButton("Визажист")
                        prof_tree = types.KeyboardButton("Иллюстратор")
                        prof_fr = types.KeyboardButton("Модель")
                        prof_fi = types.KeyboardButton("Фотомодель")
                        prof_six = types.KeyboardButton("Фотограф")
                        prof_sev = types.KeyboardButton("Танцор")
                        prof_ete = types.KeyboardButton("Вокалист")
                        prof_nine = types.KeyboardButton("Гитарист")
                        prof_ten = types.KeyboardButton("Композитор")
                        prof_eleven = types.KeyboardButton("Режиссёр")
                        prof_twelw = types.KeyboardButton("Танцор")
                        prof_trinadtcat = types.KeyboardButton("Флорист")
                        prof_fotin = types.KeyboardButton("Художник")
                       
                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten,prof_eleven,prof_twelw ,prof_trinadtcat ,prof_fotin )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)       

                        
                        
                    if message.text == "Профессии сервиса (обслуживания)":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Мастер педикюра")
                        prof_one = types.KeyboardButton("Манекенщица")
                        prof_two = types.KeyboardButton("Парикмахер")
                        prof_tree = types.KeyboardButton("Повар")
                        prof_fr = types.KeyboardButton("Бармен")
                        prof_fi = types.KeyboardButton("Горничная")
                        prof_six = types.KeyboardButton("Грузчик")
                        prof_sev = types.KeyboardButton("Кладовщик")
                        prof_ete = types.KeyboardButton("Курьер")
                        prof_nine = types.KeyboardButton("Няня")
                        prof_ten = types.KeyboardButton("Официант")
                        prof_eleven = types.KeyboardButton("Продавец")
                        prof_twelw = types.KeyboardButton("Сиделка")
                        prof_trinadtcat = types.KeyboardButton("Упаковщик")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten, prof_eleven,prof_twelw ,prof_trinadtcat )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro) 

                        
                    
                    if message.text == "Юридические, правоохранительные (МЧС, МВД)":
                        nabor_pro=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        mosck = types.KeyboardButton("Адвокат")
                        prof_one = types.KeyboardButton("Кинолог")
                        prof_two = types.KeyboardButton("Государственный исполнитель")
                        prof_tree = types.KeyboardButton("Нотариус")
                        prof_fr = types.KeyboardButton("Правовед")
                        prof_fi = types.KeyboardButton("Прокурор")
                        prof_six = types.KeyboardButton("Работник органов ЗАГСа")
                        prof_sev = types.KeyboardButton("Телохранитель")
                        prof_ete = types.KeyboardButton("Юрисконсульт")
                        prof_nine = types.KeyboardButton("Юрист")
                        prof_ten = types.KeyboardButton("Таможенник")

                        nabor_pro.add(prof_one,prof_two,prof_tree,prof_fr,prof_fi,prof_six,prof_sev,prof_ete,prof_nine,prof_ten )
                        await bot.send_message(message.chat.id, "Выбери свое направление обучения или направление обучение?", reply_markup=nabor_pro)      

                       
                        
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

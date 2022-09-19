from ast import Str
from email import message
from unicodedata import name
import telebot
from telebot import types
import parzinh_hh 
import time
import schedule



bot_Token = telebot.TeleBot("")
print(message)

#def start(message):
 #   name= f"Привет, {message.from_user.first_name} {message.from_user.last_name}"
 #   bot_Token.send_message(message.chat.id, name)


#@bot_Token.message_handler(content_types=["text"])
@bot_Token.message_handler(commands=["start"])
def user_otvet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    cnopka_start=types.KeyboardButton("Начать поиск")
    markup.add(cnopka_start)
    bot_Token.send_message(message.chat.id, "Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий", reply_markup=markup)
    # photo = open("one.jpg", "rb")
    # bot_Token.send_photo(message.chat.id, photo)

@bot_Token.message_handler(content_types=["text"])   
def prozez_poizka(message):
    if message.text == "Начать поиск":
        den = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        finanze = types.KeyboardButton("Финансы и Экономика")
        urizt = types.KeyboardButton("Юриспруденция")
        den.add(finanze, urizt)
        bot_Token.send_message(message.chat.id, "Какое твое направление обучения", reply_markup=den)
        


    if message.text == "Финансы и Экономика":
        # vigruzka(message)
        for a in parzinh_hh.get_links("финансист+студент"):
            spisok=(parzinh_hh.get_resume(a))
            time.sleep(1)
            snils=str(spisok["Вакансия"])
            snils_one=str(spisok["Ссылка"])
            snils_TRY=str(spisok["Дата публикации"])
            bot_Token.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
        for a in parzinh_hh.get_links("экономист+студент"):
            spisok=(parzinh_hh.get_resume(a))
            time.sleep(1)
            snils=str(spisok["Вакансия"])
            snils_one=str(spisok["Ссылка"])
            snils_TRY=str(spisok["Дата публикации"])
            bot_Token.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
            # vosvrat()
          
    if message.text == "Юриспруденция":
            for a in parzinh_hh.get_links("юрист+студент"):
                spisok=(parzinh_hh.get_resume(a))
                time.sleep(1)
                snils=str(spisok["Вакансия"])
                snils_one=str(spisok["Ссылка"])
                snils_TRY=str(spisok["Дата публикации"])
                bot_Token.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
            for a in parzinh_hh.get_links("начинающий+юрист"):
                spisok=(parzinh_hh.get_resume(a))
                time.sleep(1)
                snils=str(spisok["Вакансия"])
                snils_one=str(spisok["Ссылка"])
                snils_TRY=str(spisok["Дата публикации"])
                bot_Token.send_message(message.chat.id,f"Вакансия:{snils}\nСсылка:{snils_one}\nДата публикации:{snils_TRY}" )
                # vosvrat()
    
    # def vosvrat():    
    #     fp = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    #     start=types.KeyboardButton('/start')
    #     fp.add(start)
                


# def vigruzka(message):
#     meg = types.ReplyKeyboardMarkup()
#     ned = types.KeyboardButton("Получить вакансии за последние две недели")
#     date = types.KeyboardButton("Отлеживать вакансии с сегодняшнего дня")
#     meg.add(ned, date)
#     bot_Token.send_message(message.chat.id, "Какое тебе удобнее получить вакансии", reply_markup=meg)


bot_Token.polling(none_stop=True)

def main():
    schedule.every(30).minute.do(bot_Token.polling(none_stop=True))
        
       
if __name__ == "__main__":
    main()
from aiogram import types, Dispatcher 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.types import ChatMemberMember, ChatMemberAdministrator,ChatMemberOwner
from create_bot import dp , bot
from keyboards import client_k
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMvib(StatesGroup):
        sity = State()
        sfera = State()
        profesion = State()



# @dp.message_handler(commands=["start"])


# @dp.message_handler(content_types=["text"])   
async def bot_message(message: types.Message):
        user_status = await bot.get_chat_member(chat_id="@prolet_te", user_id=message.from_user.id)
        
        if isinstance(user_status, ChatMemberMember) or isinstance(user_status, ChatMemberAdministrator) or isinstance(user_status, ChatMemberOwner):
            kap = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            cnopka_start = types.KeyboardButton("Начать поиск")
            kap.add(cnopka_start)
            await bot.send_message(message.chat.id,
                                   "Приветствую студент или недавно закончивший ВУЗ. Этот бот поможет тебе найти подходящие вакансии на HH.ru без твоего ручного поиска. Тебе останется лишь отправлять резюме и пройти собеседование. Удачи в поисках""Главный разработчик:Шапранов Дмитрий",
                                   reply_markup=kap)
        else:
                bt_silca_na_canal= InlineKeyboardMarkup()
                butt= types.InlineKeyboardButton(text="Подпишись",url="https://t.me/prolet_te")
                bt_silca_na_canal.add(butt)
                await bot.send_message(message.chat.id,"Привет для начала использования бота потребентся подписатся на наш канал",reply_markup=bt_silca_na_canal)

async def cm_sity(message:types.Message):
        await FSMvib.sity.set()
        await bot.send_message(message.chat.id, "Город в котором вы ищете работу", reply_markup=client_k.nabor_sity)
async def sity_otv(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['sity'] = message.text
    await FSMvib.next()
    await bot.send_message(message.chat.id, "Выбери сферу к которой относится твоя профессия", reply_markup=client_k.nabor_sferi)


async def sfera(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["sfera"]=message.text
    await FSMvib.next()
    await bot.send_message(message.chat.id, "Выбери проффесию поиска", reply_markup=client_k.spis_kay[data["sfera"]])
    # async with state.proxy() as data:
    #     await message.reply(str(data))

async def profesion(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data["profesion"]=message.text
        await message.reply(str(data))



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(bot_message,commands=["start"])
    dp.register_message_handler(cm_sity,text=["Начать поиск"],state=None)
    dp.register_message_handler(sity_otv, content_types=["text"], state=FSMvib.sity)
    dp.register_message_handler(sfera, content_types=["text"], state=FSMvib.sfera)
    dp.register_message_handler(profesion, content_types=["text"], state=FSMvib.profesion)

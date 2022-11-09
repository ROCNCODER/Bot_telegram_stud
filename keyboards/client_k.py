from aiogram.types import ReplyKeyboardMarkup, KeyboardButton             
                       

econom = KeyboardButton("Экономические профессии")
med = KeyboardButton("Медицинские профессии")
it = KeyboardButton("IT профессии ")
ingen = KeyboardButton("Технические\Инженерные/строительные профессии/ручной труд")
since = KeyboardButton("Научные профессии")
trans = KeyboardButton("Транспортные профессии")
tvor = KeyboardButton("Творческие профессии")
servis = KeyboardButton("Профессии сервиса (обслуживания)")
urustick = KeyboardButton("Юридические, правоохранительны")
nabor_sferi = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
nabor_sferi.add(econom,med,it,ingen,since,trans,tvor,servis,urustick)


nabor_sity=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
mosck =   KeyboardButton("Москва и Мос область")
spb =   KeyboardButton("Санкт-Петербург")
sib =   KeyboardButton("Новосибирск")
eca =   KeyboardButton("Екатеринбург")
kaz =   KeyboardButton("Казань")
nov =   KeyboardButton("Нижний Новгород")
cheba =   KeyboardButton("Челябинск")
sam =   KeyboardButton("Самара")
perm =   KeyboardButton("Пермь")
nabor_sity.add(mosck,spb,sib,kaz,eca,nov,cheba,sam,perm )






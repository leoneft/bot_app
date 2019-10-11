import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,  KeyboardButton


mark1 = InlineKeyboardMarkup()
mark1.row_width = 2
mark1.add(InlineKeyboardButton("Да", callback_data="y0"), InlineKeyboardButton("Нет", callback_data="n0"))

m1 = ReplyKeyboardMarkup(resize_keyboard=True)
m1.add(KeyboardButton("📲 Доступные для загрузки приложения"))
m1.add(KeyboardButton("✉ Пригласить друга"), KeyboardButton('📃 Личный кабинет'))

m2 = ReplyKeyboardMarkup(resize_keyboard=True)
m2.add(KeyboardButton("⬅ Главное меню"))

m4 = ReplyKeyboardMarkup(one_time_keyboard=True)
m4.row_width = 1
m4.add(KeyboardButton('Joom – товары из Китая [Android 5.0+]'))
m4.add(KeyboardButton('Joom – покупай и экономь! [IOS]'))
m4.add(KeyboardButton('Auto.ru [Android 5.0+]'))
m4.add(KeyboardButton('Auto.ru [IOS]'))
m4.add(KeyboardButton('Winline [IOS]'))
m4.add(KeyboardButton('Париматч: ставки на спорт [IOS]'))
m4.add(KeyboardButton('Book of Slots [IOS]'))
m4.add(KeyboardButton("⬅ Главное меню"))

md1 = InlineKeyboardMarkup()
md1.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=1071'))
md1.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md1.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md2 = InlineKeyboardMarkup()
md2.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=1072'))
md2.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md2.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md3 = InlineKeyboardMarkup()
md3.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=2236'))
md3.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md3.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md4 = InlineKeyboardMarkup()
md4.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=2237'))
md4.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md4.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md5 = InlineKeyboardMarkup()
md5.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=3100'))
md5.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md5.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md6 = InlineKeyboardMarkup()
md6.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=3217'))
md6.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md6.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))

md7 = InlineKeyboardMarkup()
md7.add(InlineKeyboardButton(text='Скачать', url='https://track.zorkanetwork.com/click?pid=8141&offer_id=3270'))
md7.add(InlineKeyboardButton(text='⬅ Главное меню', callback_data="home"))
md7.add(InlineKeyboardButton(text='📲 Доступные для загрузки приложения',callback_data="apps"))




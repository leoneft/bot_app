import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

mark1 = InlineKeyboardMarkup()
mark1.row_width = 2
mark1.add(InlineKeyboardButton("Да", callback_data="y0"), InlineKeyboardButton("Нет", callback_data="n0"))

m1 = ReplyKeyboardMarkup(resize_keyboard=True)
m1.add(KeyboardButton("📲 Доступные для загрузки приложения"))
m1.add(KeyboardButton("✉ Пригласить друга"), KeyboardButton('📃 Информация'))

m2 = ReplyKeyboardMarkup(resize_keyboard=True)
m2.add(KeyboardButton("⬅ Главное меню"))

m4 = ReplyKeyboardMarkup()
m4.row_width = 1
m4.add(KeyboardButton('Joom – товары из Китая [Android 5.0+]'))
m4.add(KeyboardButton('Joom – покупай и экономь! [IOS]'))
m4.add(KeyboardButton('Auto.ru [Android 5.0+]'))
m4.add(KeyboardButton('Auto.ru [IOS]'))
m4.add(KeyboardButton('Winline [IOS]'))
m4.add(KeyboardButton('Париматч: ставки на спорт [IOS]'))
m4.add(KeyboardButton('Book of Slots [IOS]'))

md1 = ReplyKeyboardMarkup(resize_keyboard=True)
md1.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md1.add(KeyboardButton("⬇ Скачать Joom[Android]"))
md1.add(KeyboardButton("⬅ Главное меню"))

md2 = ReplyKeyboardMarkup(resize_keyboard=True)
md2.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md2.add(KeyboardButton("⬇ Скачать Joom[IOS]"))
md2.add(KeyboardButton("⬅ Главное меню"))

md3 = ReplyKeyboardMarkup(resize_keyboard=True)
md3.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md3.add(KeyboardButton("⬇ Скачать Auto.ru[Android]"))
md3.add(KeyboardButton("⬅ Главное меню"))

md4 = ReplyKeyboardMarkup(resize_keyboard=True)
md4.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md4.add(KeyboardButton("⬇ Скачать Auto.ru[IOS]"))
md4.add(KeyboardButton("⬅ Главное меню"))

md5 = ReplyKeyboardMarkup(resize_keyboard=True)
md5.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md5.add(KeyboardButton("⬇ Скачать Winline [IOS]"))
md5.add(KeyboardButton("⬅ Главное меню"))

md6 = ReplyKeyboardMarkup(resize_keyboard=True)
md6.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md6.add(KeyboardButton("⬇ Скачать Париматч: ставки на спорт [IOS]"))
md6.add(KeyboardButton("⬅ Главное меню"))

md7 = ReplyKeyboardMarkup(resize_keyboard=True)
md7.add(KeyboardButton("📲 Доступные для загрузки приложения"))
md7.add(KeyboardButton("⬇ Скачать Book of Slots [IOS]"))
md7.add(KeyboardButton("⬅ Главное меню"))

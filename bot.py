import telebot
import markups
import shelve
import random


token = '980366787:AAEPskwam0HqmW3eUjfaD4dkw5IGA4LkxE4'
bot = telebot.TeleBot(token)
links = ['https://track.zorkanetwork.com/click?pid=8141&offer_id=1071',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=1072',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=2236',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=2237',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=3100',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=3217',
         'https://track.zorkanetwork.com/click?pid=8141&offer_id=3270']


def manager(message):
    db = shelve.open('db', writeback=True)
    db[str(message.chat.id)]['num_of_apps'] += 1
    db.close()


@bot.message_handler(commands=['start'])
def send(message):
    if message.text == '/start':
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        cid = message.chat.id
        db = shelve.open('db', writeback=True)
        db[str(message.chat.id)] = dict()
        db.close()
        mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        bot.send_message(cid, " Привет, " + mention + '! ' + 'Для начала укажи номер телефона в формате +79123456789. Если к нему привязан Qiwi кошелек, мы отправим вознаграждения на него. Если нет - на номер телефона.', parse_mode="Markdown")
        bot.register_next_step_handler(message, number)


def number(message):
    db = shelve.open('db', writeback=True)
    db[str(message.chat.id)]['num_of_apps'] = 0
    db[str(message.chat.id)]['balance'] = 30
    db[str(message.chat.id)]['phone'] = str(message.text)
    bot.send_message(message.chat.id, f"Ваш телефон: {db[str(message.chat.id)]['phone']} ", reply_markup=markups.mark1)
    db.close()


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "y0":
        bot.send_message(call.message.chat.id, 'Аккаунт создан.\nУдачи!', reply_markup=markups.m1)
    elif call.data == "n0":
        msg = bot.send_message(call.message.chat.id, 'Заново введи номер телефона.')
        bot.register_next_step_handler(msg, number)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "✉ Пригласить друга":
        bot.send_message(message.chat.id, f'За каждого друга, выполнившего хотя бы одно задание вы получите 40 рублей.\nВаша ссылка для приглашения:  t.me/CashForAppsBot?start\nСкопируйте ее и отправьте друзьям, у которых есть telegram.', reply_markup=markups.m2 )
    elif message.text == "⬅ Главное меню":
        bot.send_message(message.chat.id, 'Главное меню.\n', reply_markup=markups.m1)
    elif message.text == '📃 Информация':
        db = shelve.open('db', writeback=True)
        bot.send_message(message.chat.id, f"Информация:\nТелефон: {db[str(message.chat.id)]['phone']}.\nБаланс: {db[str(message.chat.id)]['balance']} рублей.\n\nДеньги будут начислятся через некоторое время после установки приложения.\nВывод происходит автоматически, как только вы заработаете хотя бы 100 рублей.\nАктивных пользователей: {(2500 + random.randint(-100, 100))}.\nСредний зароботок за месяц: {(8000 + random.randint(-100, 100))} рублей.", reply_markup=markups.m2)
        db.close()
    elif message.text == "📲 Доступные для загрузки приложения":
        bot.send_message(message.chat.id, 'Список приложений:', reply_markup=markups.m4)
    elif message.text == 'Joom – товары из Китая [Android 5.0+]':
        text = '*Joom – товары из Китая*\nЗ*адание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* Android 5.0+\n*Геотаргетинг:* Россия, Белоруссия, Украина, Казахстан\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id, f'[​​​​​​​​​​​](https://lh3.googleusercontent.com/9rejlDV7rmxBhqgpPzTPozieMKzFH1c3L7ybosBPou6N4AriULYJGeEoBllF7RmNzVA=s360-rw){text}',
                         reply_markup=markups.md1, parse_mode='markdown')
    elif message.text =='Joom – покупай и экономь! [IOS]':
        text = '*Joom – покупай и экономь*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* IOS 9.0+\n*Геотаргетинг:* Россия, Белоруссия, Украина, Казахстан и другие страны.\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://lh3.googleusercontent.com/9rejlDV7rmxBhqgpPzTPozieMKzFH1c3L7ybosBPou6N4AriULYJGeEoBllF7RmNzVA=s360-rw){text}',
                         reply_markup=markups.md2, parse_mode='markdown')
    elif message.text =='Auto.ru [IOS]':
        text = '*Auto.ru*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* IOS 9.0+\n*Геотаргетинг:* Россия\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://i0.wp.com/apptractor.ru/wp-content/uploads/2016/06/autoru.png?fit=512%2C512&ssl=1){text}',
                         reply_markup=markups.md4, parse_mode='markdown')
    elif message.text =='Auto.ru [Android 5.0+]':
        text = '*Auto.ru*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* Android 5.0+\n*Геотаргетинг:* Россия\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://i0.wp.com/apptractor.ru/wp-content/uploads/2016/06/autoru.png?fit=512%2C512&ssl=1){text}',
                         reply_markup=markups.md3, parse_mode='markdown')
    elif message.text =='Winline [IOS]':
        text = '*Winline*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* IOS 9.0+\n*Геотаргетинг:* Россия\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://betonmobile.ru/wp-content/uploads/2017/06/winline_maxi.png){text}',
                         reply_markup=markups.md5, parse_mode='markdown')
    elif message.text =='Париматч: ставки на спорт [IOS]':
        text = '*Париматч: ставки на спорт*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформа:* IOS 9.0+\n*Геотаргетинг:* Россия\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://parimatchbk3.com/wp-content/uploads/2019/08/%D0%A1%D1%82%D0%B0%D0%B2%D0%BA%D0%B8-%D0%B2-%D0%B1%D1%83%D0%BA%D0%BC%D0%B5%D0%BA%D0%B5%D1%80%D1%81%D0%BA%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D0%BE%D1%80%D0%B5-Parimatch-1.jpg){text}',
                         reply_markup=markups.md6, parse_mode='markdown')
    elif message.text =='Book of Slots [IOS]':
        text = '*Book of Slots*\n*Задание:*\n*- Скачать приложение, не заходить в него*\n*- Подождать 30-60 сек*\n*- Зайти в него*\n*По желанию:* зарегистрироваться и не удалять пару дней.\n*Платформы:* IOS 9.0+\n*Геотаргетинг:* Россия\n*Плата за установку:* 25 рублей.'
        bot.send_message(message.chat.id,
                         f'[​​​​​​​​​​​](https://casinogamesonnet.com/images/slots/book-of-magic-slot-screen.jpg){text}',
                         reply_markup=markups.md7, parse_mode='markdown')
    elif message.text =="⬇ Скачать Joom[Android]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[0]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Joom[IOS]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[1]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Auto.ru[Android]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[3]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Auto.ru[IOS]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[2]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Winline [IOS]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[4]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Париматч: ставки на спорт [IOS]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[5]}\n ', reply_markup=markups.m2)
        manager(message)
    elif message.text =="⬇ Скачать Book of Slots [IOS]":
        bot.send_message(message.chat.id, f'Ваша ссылка для скачивания: {links[6]}\n ', reply_markup=markups.m2)
        manager(message)


bot.polling(none_stop=True)

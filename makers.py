import telebot
from telebot import types
from string import Template
import urllib.request, urllib.parse
import datetime
from datetime import date



token = "935817554:AAHWc2Gnvj50Lup4dhPjVf9cz7_P4pJXg2Q"
bot = telebot.TeleBot(token)



entry = {}

entry1 = {}


class User:
    def __init__(self, account):
        self.account = account

        keys = ['name', 'date', 'summ', 'wallet', 'direct', 'contragent', 'purpose_of_payment', 'comment']
        for key in keys:
            self.key = None




@bot.message_handler(commands=["start"])
def proccess_user(message):
    try:
        chat_id = message.chat.id
        entry[chat_id] = User(message.text)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Нурц')
        btn2 = types.KeyboardButton('Айба')
        markup.add(btn1, btn2)

        msg = bot.send_message(chat_id, "Кто вы?: ", reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_name) 

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooops!!')




def proccess_name(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.name = message.text
        entry1['name'] = message.text

        markup = types.ReplyKeyboardRemove(selective=False)
        # keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        # btn1 = types.KeyboardButton('Вчера', callback='yesterday')
        # btn2 = types.KeyboardButton('Сегодня', callback='today')
        # keyboard.add(btn1, btn2)

        msg = bot.send_message(chat_id, "Укажите дату: ")
        bot.register_next_step_handler(msg, proccess_date)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooops!!')




def proccess_date(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.date = message.text.replace(" ", ".")
        # entry1['date'] = message.text.replace(" ", ".")
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, "Укажите сумму: ")
        bot.register_next_step_handler(msg, proccess_summ)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooops!!')




def proccess_summ(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.summ = message.text
        entry1['summ'] = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        first_btn = types.KeyboardButton('Наличные')
        second_btn = types.KeyboardButton('Карта')
        third_btn = types.KeyboardButton('Элсом')
        markup.add(first_btn, second_btn, third_btn)


        msg = bot.send_message(chat_id, "Выберите тип: ", reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_wallet)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def proccess_wallet(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.wallet = message.text
        entry1['wallet'] = message.text

        markup = types.ReplyKeyboardRemove(selective=False)
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("Общее")
        keyboard.add(btn1)


        msg = bot.send_message(chat_id, 'Укажите направление: ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, proccess_direct)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def proccess_direct(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.direct = message.text
        entry1['direct'] = message.text

        makrup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Укажите контрагента: ', reply_markup=makrup)
        bot.register_next_step_handler(msg, proccess_contragent)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def proccess_contragent(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.contragent = message.text
        entry1['contragent'] = message.text

        msg = bot.send_message(chat_id, 'Укажите назначение платежа: ')
        bot.register_next_step_handler(msg, proccess_purpose_of_payment)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def proccess_purpose_of_payment(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.purpose_of_payment = message.text
        entry1['purpose_of_payment'] = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        first_btn = types.KeyboardButton('Поступления от клиента')
        second_btn = types.KeyboardButton('Прочие поступления')
        third_btn = types.KeyboardButton('Поставщики транспортных услуг')
        fourth_btn = types.KeyboardButton('Аренда офиса')
        fifth_btn = types.KeyboardButton('Содержание офиса')
        sixth_btn = types.KeyboardButton('Удобства обучения')
        seventh_btn = types.KeyboardButton('Зарплата менторов/скрамов/трекеров')
        eighth_btn = types.KeyboardButton('РКО')
        nineth_btn = types.KeyboardButton('Связь и интернет')
        tenth_btn = types.KeyboardButton('Приобретение оргтехники')
        eleventh_btn = types.KeyboardButton('Поиск персонала')
        twelveth_btn = types.KeyboardButton('Зарплата коммерческого персонала')
        markup.add(first_btn, second_btn, third_btn, fourth_btn, fifth_btn, sixth_btn, seventh_btn, eighth_btn, nineth_btn, tenth_btn, eleventh_btn, twelveth_btn)

        msg = bot.send_message(chat_id, 'Укажите комментарий: ', reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_comment)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def proccess_comment(message):
    try:
        chat_id = message.chat.id
        user = entry[chat_id]
        user.comment = message.text
        entry1['comment'] = message.text

        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")

    except Exception as e:
        print(e)
        bot.reply_to(message, 'ooopps!!!')




def getRegData(user, title, name):
    try:
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdpJXdz95GoF0D0G9joogYT5dI7Zdx8eJzkVms4myyV_Twg1w/formResponse"
        data = {
            'entry.1858411408': user.name, 
            'entry.58745814': user.date, 
            'entry.1013804646': user.summ, 
            'entry.2097473245': user.wallet,
            'entry.1710730194': user.direct,
            'entry.901100001': user.contragent,
            'entry.1362601104': user.purpose_of_payment,
            'entry.1674378938': user.comment
            }
        data = bytes( urllib.parse.urlencode(data).encode())
        handler = urllib.request.urlopen(url, data)
        t = Template('$title *$name* \n Имя: *$name* \n Дата: *$date* \n Сумма: *$summ* \n Кошелек: *$wallet* \n Направление: *$direct* \n Контрагент: *$contragent* \n Назначение платежа: *$purpose_of_payment* \n Комментарий: *$comment*')
        return t.substitute({
            'title': title,
            'name': name,
            'UserAccount': user.account,
            'name': user.name,
            'date': user.date,
            'summ': user.summ,
            'wallet': user.wallet,
            'direct': user.direct,
            'contragent': user.contragent,
            'purpose_of_payment': user.purpose_of_payment,
            'comment': user.comment
        })
    except Exception as e:
        print(e)


# @bot.callback_query_handler(func=lambda call:True)
# def time(callback):
#     data = callback.data
#     if callback.data == 'today':
#         date.today()
#     if callback.data == 'yesterday':
#         date.

# def post():
#     print(entry1)
#     url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdpJXdz95GoF0D0G9joogYT5dI7Zdx8eJzkVms4myyV_Twg1w/formResponse"
#     data = {
#         'entry.1858411408': entry1['name'], 
#         'entry.58745814': entry1['date'], 
#         'entry.1013804646': entry1['summ'], 
#         'entry.2097473245': entry1['wallet'],
#         'entry.1710730194': entry1['direct'],
#         'entry.901100001': entry1['contragent'],
#         'entry.1362601104': entry1['purpose_of_payment'],
#         'entry.1674378938': entry1['comment']
#         }
#     data = bytes( urllib.parse.urlencode(data).encode())
#     handler = urllib.request.urlopen(url, data)



# bot.enable_save_next_step_handlers(delay=2)

# bot.load_next_step_handlers()


    
if __name__ == '__main__':
    bot.polling(none_stop=True)





# =IMPORTRANGE("https://docs.google.com/spreadsheets/d/1apQFTG_KiEDxd0eQmO-9LlDsBfnGUoZ7-2QMFK_seTk/edit#gid=1228125165"; "C2:I8")












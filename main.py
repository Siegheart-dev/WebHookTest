import telebot
import os
from telebot import types



bot = telebot.TeleBot('5070280174:AAEn7rvSorr71jDZSDL9GaBzt439F-YC5Nw')
main_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_book = types.KeyboardButton(text="Записаться на мойку")
button_price = types.KeyboardButton(text="Прайс-лист ваших услуг")
button_venue = types.KeyboardButton(text="Где вы находитесь?")
button_contact = types.KeyboardButton(text="Контактные данные ваших менеджеров")
main_menu.add(button_book,button_price,button_venue,button_contact)
bot.delete_webhook()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        print(message.text),print(message.from_user.first_name)

        bot.send_message(message.from_user.id, 'Привет ' + message.from_user.first_name + ', я бот Фрэш Авто',
                         reply_markup=main_menu)
    elif message.text == 'Записаться на мойку':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        button_menu = types.KeyboardButton(text="Возврат в главное меню")
        #button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_phone,button_menu)
        bot.send_message(message.chat.id,
                         "Укажите свой номер телефона и наши менеджеры с Вами свяжутся",
                         reply_markup=keyboard)
    elif message.text == 'Прайс-лист ваших услуг':
        bot.send_message(message.chat.id,'Выгружаем Вам прайс-лист,пожалуйста подождите')
        bot.send_document(message.chat.id,'https://i.ibb.co/Qf2SXCM/Price-List.jpg')
    elif message.text == 'Возврат в главное меню':
        bot.send_message(message.from_user.id,'Возвращаемся в главное меню', reply_markup=main_menu)
    elif message.text == 'Где вы находитесь?':
        bot.send_venue(message.from_user.id, 46.421665, 30.726447, "Фрэш Авто","Люстдорфсая дорога, 55-а, г.Одесса, Украина")
    elif message.text == 'Контактные данные ваших менеджеров':
        bot.send_contact(message.from_user.id,phone_number=+380739401234,first_name='Фрэш Авто')

@bot.message_handler(content_types=['contact'])
def get_contact_messages(message):
    id = message.from_user.id
    print(id)
    bot.forward_message(chat_id='-1001780484687',from_chat_id=message.from_user.id,
                       message_id=message.message_id)
    bot.send_message(message.from_user.id, 'Ваша заявка принята!', reply_markup=main_menu)



bot.polling(none_stop=True,interval=0,timeout=100)

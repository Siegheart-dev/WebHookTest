import telegram
from telegram import KeyboardButton


class Button:
    def buttons_main_menu(self):
        button1 = 'Записаться на мойку'
        button2 = 'Прайс-лист ваших услуг'
        button3 = 'Где вы находитесь?'
        button4 = 'Контактные данные ваших менеджеров'
        buttons = [[KeyboardButton(button1)],[KeyboardButton(button2)],[KeyboardButton(button3)],[KeyboardButton(button4)]]
        main_menu = telegram.ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)
        return main_menu
    def buttons_sec_menu(self):
        button_1 = 'Отправить номер телефона'
        button_2 = 'Возврат в главное меню'
        buttons2=[[KeyboardButton(button_1,request_contact=True)],[KeyboardButton(button_2)]]
        send_cont_menu = telegram.ReplyKeyboardMarkup(keyboard=buttons2,resize_keyboard=True)
        return send_cont_menu
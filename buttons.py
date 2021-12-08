import telegram
from telegram import KeyboardButton

class Button:
    def buttons_main_menu(self):
        buttons = [[KeyboardButton('Записаться на мойку')],[KeyboardButton('Прайс-лист ваших услуг')],[KeyboardButton('Где вы находитесь?')],[KeyboardButton('Контактные данные ваших менеджеров')]]
        main_menu = telegram.ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)
        return main_menu
    def buttons_sec_menu(self):
        buttons2=[[KeyboardButton('Отправить номер телефона',request_contact=True)],[KeyboardButton('Возврат в главное меню')]]
        send_cont_menu = telegram.ReplyKeyboardMarkup(keyboard=buttons2,resize_keyboard=True)
        return send_cont_menu
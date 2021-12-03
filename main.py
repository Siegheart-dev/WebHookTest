import os

import telegram
from telegram import Update,KeyboardButton, ReplyMarkup
from telegram.ext import Updater ,CommandHandler,Dispatcher,CallbackContext,MessageHandler,Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
TOKEN = "2109220948:AAGxs3OFTIeqHsRam7t1BfNVNDsObsQQCLo"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN ,use_context=True)
# add handlers
dispatcher = updater.dispatcher

button1 = 'Прайс-лист ваших услуг'
button2 = 'asdad'
#keyboard_seq = [[['Прайс-лист ваших услуг',KeyboardButton]]]
buttons = [[KeyboardButton(button1)],[KeyboardButton(button2)]]
main_menu = telegram.ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)


def start(update: Update, context: CallbackContext):

    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!",reply_markup=main_menu)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    chat_text = update.message.text
    if chat_text == 'Прайс-лист ваших услуг':
        context.bot.send_document(chat_id=update.effective_chat.id, document='https://i.ibb.co/Qf2SXCM/Price-List.jpg')
    if chat_text == 'Где вы находитесь?':
        context.bot.send_venue(chat_id=update.effective_chat.id, latitude=46.421665, longitude=30.726447,
                               title="Фрэш Авто", address="Люстдорфсая дорога, 55-а, г.Одесса, Украина")
    if chat_text == 'Контактные данные ваших менеджеров':
        context.bot.send_contact(chat_id=update.effective_chat.id, phone_number=+380739401234,first_name='Фрэш Авто')
    if chat_text == 'Возвращаемся в главное меню':
        context.bot.send_message(chat_id=update.effective_chat.id, text='update.message.text')


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://webhooktester19.herokuapp.com/" + TOKEN)
updater.idle()
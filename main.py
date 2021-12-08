import os
import telegram
from telegram import Update,KeyboardButton, ReplyMarkup
from telegram.ext import Updater ,CommandHandler,Dispatcher,CallbackContext,MessageHandler,Filters
import logging
from buttons import Button

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
TOKEN = "5070280174:AAEn7rvSorr71jDZSDL9GaBzt439F-YC5Nw"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN ,use_context=True)
# add handlers
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!",reply_markup=Button().buttons_main_menu())
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def chat_messages(update: Update, context: CallbackContext):
    chat_text = update.message.text
    if chat_text == 'Записаться на мойку':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Чтобы оставить заявку - нажмите кнопку отправить номер телефона, затем всплывет окно"
                         " после чего нажмите 'ok' либо 'Share'", reply_markup=Button().buttons_sec_menu())
    if chat_text == 'Прайс-лист ваших услуг':
        context.bot.send_document(chat_id=update.effective_chat.id, document='https://i.ibb.co/Qf2SXCM/Price-List.jpg')
    if chat_text == 'Где вы находитесь?':
        context.bot.send_venue(chat_id=update.effective_chat.id, latitude=46.421665, longitude=30.726447,
                               title="Фрэш Авто", address="Люстдорфсая дорога, 55-а, г.Одесса, Украина")
    if chat_text == 'Контактные данные ваших менеджеров':
        context.bot.send_contact(chat_id=update.effective_chat.id, phone_number=+380739401234,first_name='Фрэш Авто')
    if chat_text == 'Возврат в главное меню':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Возвращаемся в главное меню...',reply_markup=Button().buttons_main_menu())

chat_handler = MessageHandler(Filters.text & (~Filters.command), chat_messages)
dispatcher.add_handler(chat_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://webhooktester19.herokuapp.com/" + TOKEN)
updater.idle()
import os
from telegram import Update
from telegram.ext import Updater ,CommandHandler,Dispatcher,CallbackContext,MessageHandler,Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
TOKEN = "2109220948:AAGxs3OFTIeqHsRam7t1BfNVNDsObsQQCLo"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN ,use_context=True)
# add handlers
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)


def reply(update: Update, context: CallbackContext):
    if update.effective_message.text == 'Где':
       context.bot.send_venue(chat_id=update.effective_chat.id, latitude=46.421665, longtitude=30.726447, title="Фрэш Авто",adress="Люстдорфсая дорога, 55-а, г.Одесса, Украина")

reply_handler = MessageHandler(Filters.text,reply)
dispatcher.add_handler(echo_handler)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://webhooktester19.herokuapp.com/" + TOKEN)
updater.idle()
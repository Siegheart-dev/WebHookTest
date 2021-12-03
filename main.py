import os
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext

TOKEN = "2109220948:AAGxs3OFTIeqHsRam7t1BfNVNDsObsQQCLo"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")



updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://webhooktester19.herokuapp.com/" + TOKEN)
updater.idle()
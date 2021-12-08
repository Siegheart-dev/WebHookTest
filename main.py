import os
from telegram import Update
from telegram.ext import Updater ,CommandHandler,CallbackContext,MessageHandler,Filters
import logging
from buttons import Button
from reference import Ref

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# add handlers
dispatcher = Ref().updater_context().dispatcher
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет "+update.effective_chat.first_name+ ",я бот Фрэш Авто",reply_markup=Button().buttons_main_menu())
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def chat_message_handler(update: Update, context: CallbackContext):
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
def contact_handler(update: Update, context: CallbackContext):
        context.bot.send_contact(chat_id=-1001780484687,phone_number=update.effective_message.contact.phone_number,first_name=update.effective_message.contact.first_name)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ваша заявка принята,наши менеджеры с Вами свяжутся!')

dispatcher.add_handler(MessageHandler(Filters.contact,contact_handler))
chat_handler = MessageHandler(Filters.text & (~Filters.command), chat_message_handler)
dispatcher.add_handler(chat_handler)

Ref().updater_context().start_webhook("0.0.0.0",
                      Ref().port(),
                      Ref().token(),
                      webhook_url="https://webhooktester19.herokuapp.com/" + Ref().token())
Ref().updater_context().idle()
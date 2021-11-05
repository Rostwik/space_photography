# @Space_photography_bot
import os

from telegram import Update, bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv('TELEGRAM_TOKEN')


def get_bot_info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{context.bot.get_me()}')


def start(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(
        chat_id='@whydoesapersonnotsitathome',
        text='Всем привет!'
    )
    photo = open('images/epic_1b_20211104000830.png', 'rb')
    context.bot.send_photo(
        chat_id='@whydoesapersonnotsitathome',
        caption=f'Фото',
        photo=photo,
    )


updater = Updater(telegram_bot_token)

updater.dispatcher.add_handler(CommandHandler('get_bot_info', get_bot_info))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

# @Space_photography_bot
import os
from os import listdir

from telegram import Update, bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

from fetch_nasa import download_and_save_nasa_photos

load_dotenv()
nasa_api_token = os.getenv('NASA_API_TOKEN')
telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
delay_in_sending = os.getenv('DELAY_IN_SENDING')


def get_bot_info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{context.bot.get_me()}')


def start(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(
        chat_id='@whydoesapersonnotsitathome',
        text='Всем привет!'
    )


def send_photos_to_telegram_group(update: Update, context: CallbackContext):
    while True:
        directory_of_images = download_and_save_nasa_photos(nasa_api_token, int(delay_in_sending))

        pictures = listdir(directory_of_images)
        for picture in pictures:
            photo = open(f'{directory_of_images}/{picture}', 'rb')
            context.bot.send_photo(
                chat_id='@whydoesapersonnotsitathome',
                caption=f'{picture}',
                photo=photo,
            )


def main():
    updater = Updater(telegram_bot_token)
    updater.dispatcher.add_handler(CommandHandler('get_bot_info', get_bot_info))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('run_nasa', send_photos_to_telegram_group))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

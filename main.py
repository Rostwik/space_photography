# @Space_photography_bot
import os
from os import listdir

import telegram
from dotenv import load_dotenv
from fetch_nasa import download_nasa_photos
from fetch_spacex import download_spacex_launch_photos


def send_photos_to_telegram_group(bot, directory_name):
    while True:

        pictures = listdir(directory_name)

        for picture in pictures:
            photo = open(f'{directory_name}/{picture}', 'rb')
            bot.send_photo(
                chat_id='@whydoesapersonnotsitathome',
                caption=f'{picture}',
                photo=photo,
            )


def main():
    bot = telegram.Bot(token=telegram_bot_token)
    pictures_directory = 'images'
    flight_number = 45

    download_spacex_launch_photos(pictures_directory, flight_number)
    download_nasa_photos(nasa_api_token, int(delay_in_sending), pictures_directory)

    send_photos_to_telegram_group(bot, pictures_directory)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_token = os.getenv('NASA_API_TOKEN')
    telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
    delay_in_sending = os.getenv('DELAY_IN_SENDING')
    main()

import os
from os import listdir
import random
import time

import telegram
from dotenv import load_dotenv
from requests import HTTPError

from fetch_nasa import download_nasa_photos
from fetch_spacex import download_spacex_launch_photos


def send_photos_to_telegram_group(bot, directory_name, delay):
    time.sleep(delay)

    pictures = listdir(directory_name)
    random_picture = random.choice(pictures)

    photo = open(f'{directory_name}/{random_picture}', 'rb')
    bot.send_photo(
        chat_id='@whydoesapersonnotsitathome',
        caption=f'{random_picture}',
        photo=photo,
    )


def main():
    bot = telegram.Bot(token=telegram_bot_token)
    pictures_directory = 'images'
    flight_number = 46

    download_spacex_launch_photos(pictures_directory, flight_number)
    download_nasa_photos(nasa_api_token, pictures_directory)

    while True:
        send_photos_to_telegram_group(bot, pictures_directory, int(delay))


if __name__ == '__main__':
    load_dotenv()
    nasa_api_token = os.getenv('NASA_API_TOKEN')
    telegram_bot_token = os.getenv('TELEGRAM_TOKEN')
    delay = os.getenv('DELAY_IN_SENDING')

    try:
        main()
    except HTTPError as err:
        if err.response.status_code == 404:
            print('Запрашиваемый Вами адрес не существует.')
        if err.response.status_code == 401:
            print('Проверьте Ваш токен.')
        if err.response.status_code == 500:
            print('Сайт, куда Вы обращаетесь временно недоступен, попробуйте позже.')

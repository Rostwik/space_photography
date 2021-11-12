import datetime

import requests
import pathlib

from tools import get_file_name, save_photo


def download_nasa_photos(nasa_api_token, directory_name):
    pathlib.Path(directory_name).mkdir(exist_ok=True)

    payloads = {'api_key': nasa_api_token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payloads)
    response.raise_for_status()
    pictures_links = response.json()

    for link in pictures_links:
        formatted_date_image = datetime.datetime.fromisoformat(link['date'])
        formatted_date_image = formatted_date_image.strftime('%Y/%m/%d')
        image_name = link['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date_image}/png/{image_name}.png'

        save_photo(directory_name, image_name, image_url, payloads, '.png')

    payloads = {'api_key': nasa_api_token, 'count': 30}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payloads)
    response.raise_for_status()
    pictures_links = response.json()

    for link in pictures_links:
        filename_of_picture = get_file_name(link['url'])
        save_photo(directory_name, filename_of_picture[1], link['url'])




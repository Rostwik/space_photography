import datetime
import time

import requests
import pathlib


def download_nasa_photos(nasa_api_token, delay_in_sending, directory_name):
    time.sleep(delay_in_sending)

    pathlib.Path(directory_name).mkdir(exist_ok=True)

    payloads = {'api_key': nasa_api_token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payloads)
    response.raise_for_status()
    urls_of_pictures = response.json()

    for url_picture in urls_of_pictures:
        formatted_date_image = datetime.datetime.fromisoformat(url_picture['date'])
        formatted_date_image = formatted_date_image.strftime('%Y/%m/%d')
        image_name = url_picture['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date_image}/png/{image_name}.png'
        response = requests.get(image_url, params=payloads)
        response.raise_for_status()
        path_to_save = f'{directory_name}/{image_name}.png'
        with open(path_to_save, 'wb') as file:
            file.write(response.content)

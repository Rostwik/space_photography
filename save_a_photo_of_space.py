import datetime
import time

import requests
import pathlib


def download_and_save_nasa_photo(nasa_api_token, delay_in_sending):
    time.sleep(delay_in_sending)

    name_of_directory = 'images'
    pathlib.Path(name_of_directory).mkdir(exist_ok=True)

    payloads = {'api_key': nasa_api_token}
    urls_of_pictures_of_epic_nasa = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payloads).json()

    for url_picture in urls_of_pictures_of_epic_nasa:
        formatted_date_image = datetime.datetime.fromisoformat(url_picture['date'])
        formatted_date_image = formatted_date_image.strftime('%Y/%m/%d')
        image_name = url_picture['image']
        url_of_image = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date_image}/png/{image_name}.png'
        response = requests.get(url_of_image, params=payloads)
        name_of_directory = 'images'
        pathlib.Path(name_of_directory).mkdir(exist_ok=True)
        path_to_save = f'{name_of_directory}/{image_name}.png'
        with open(path_to_save, 'wb') as file:
            file.write(response.content)
    return name_of_directory

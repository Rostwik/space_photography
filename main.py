import os
import urllib

import requests
import pathlib
from dotenv import load_dotenv

load_dotenv()

nasa_api_token = os.getenv('NASA_API_TOKEN')


def get_file_extension(url_string):
    url_attributes = urllib.parse.urlsplit(url_string, scheme='', allow_fragments=True)
    url_path = urllib.parse.unquote(url_attributes.path, encoding='utf-8', errors='replace')
    print(url_path)
    file_name = os.path.split(url_path)[1]
    extension = os.path.splitext(file_name)[1]
    return extension


def fetch_spacex_last_launch():
    name_of_directory = 'images'
    pathlib.Path(name_of_directory).mkdir(exist_ok=True)

    url_api_spacex = "https://api.spacexdata.com/v3/launches/"
    response = requests.get(url_api_spacex)
    urls_of_pictures_of_launches_spacex = response.json()[60]['links']['flickr_images']

    for url_picture in urls_of_pictures_of_launches_spacex:
        filename_of_picture = url_picture.split('/')[-1]
        response = requests.get(url_picture)
        response.raise_for_status()
        path_to_save = f'{name_of_directory}/{filename_of_picture}'
        with open(path_to_save, 'wb') as file:
            file.write(response.content)


# fetch_spacex_last_launch()
# print(get_file_extension('https://example.com/txt/hello%20world.txt?v=9#python'))


payloads = {'api_key': nasa_api_token}
# payloads = {'api_key': nasa_api_token, 'count': 50}
# response = requests.get('https://api.nasa.gov/planetary/apod', params=payloads)
response = requests.get('https://api.nasa.gov/EPIC/api/natural/images', params=payloads).json()[0]
date_of_image, _ = (response['date'].replace('-', '/')).split()
image_name = response['image']
url_of_image = f'https://api.nasa.gov/EPIC/archive/natural/{date_of_image}/png/{image_name}.png'
response = requests.get(url_of_image, params=payloads)
name_of_directory = 'images'
pathlib.Path(name_of_directory).mkdir(exist_ok=True)
path_to_save = f'{name_of_directory}/{image_name}.png'
with open(path_to_save, 'wb') as file:
    file.write(response.content)

# urls_of_photo_of_space = [photo_description['url'] for photo_description in response.json()]
# name_of_directory = 'images'
# pathlib.Path(name_of_directory).mkdir(exist_ok=True)
# for url_picture in urls_of_photo_of_space:
#     filename_of_picture = url_picture.split('/')[-1]
#     response = requests.get(url_picture)
#     response.raise_for_status()
#     path_to_save = f'{name_of_directory}/{filename_of_picture}'
#     with open(path_to_save, 'wb') as file:
#         file.write(response.content)

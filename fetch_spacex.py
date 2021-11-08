import pathlib
import requests

from tools import get_file_name


def download_spacex_launch_photos(directory_name, flight_number):
    pathlib.Path(directory_name).mkdir(exist_ok=True)

    url_api_spacex = f'https://api.spacexdata.com/v3/launches/{flight_number}'
    response = requests.get(url_api_spacex)
    response.raise_for_status()
    urls_of_pictures_of_launches = response.json()['links']['flickr_images']

    for url_picture in urls_of_pictures_of_launches:
        filename_of_picture = get_file_name(url_picture)

        response = requests.get(url_picture)
        response.raise_for_status()

        path_to_save = f'{directory_name}/{filename_of_picture[1]}'
        with open(path_to_save, 'wb') as file:
            file.write(response.content)

import pathlib
import requests

from tools import get_file_name, save_photo


def download_spacex_launch_photos(directory_name, flight_number):
    pathlib.Path(directory_name).mkdir(exist_ok=True)

    api_url = f'https://api.spacexdata.com/v3/launches/{flight_number}'
    response = requests.get(api_url)
    response.raise_for_status()
    pictures_links = response.json()['links']['flickr_images']

    for link in pictures_links:
        filename_of_picture = get_file_name(link)

        save_photo(directory_name, filename_of_picture[1], link)
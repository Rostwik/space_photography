import requests
import pathlib


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


fetch_spacex_last_launch()

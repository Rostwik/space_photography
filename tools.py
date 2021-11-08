import os
import urllib


def get_file_name(url_string):
    url_attributes = urllib.parse.urlsplit(url_string, scheme='', allow_fragments=True)
    url_path = urllib.parse.unquote(url_attributes.path, encoding='utf-8', errors='replace')
    file_name = os.path.split(url_path)
    return file_name

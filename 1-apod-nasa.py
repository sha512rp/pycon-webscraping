import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

BASE_URL = 'http://apod.nasa.gov/'
FOLDER = '/home/sharp/Projects/pycon-webscraping/images/'


def main():
    url = 'http://apod.nasa.gov/apod/ap151107.html'
    archive_url = 'http://apod.nasa.gov/apod/archivepix.html'
    res = requests.get(archive_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links_to_images = soup.find_all('a')[3:]
    for i, image_tag in enumerate(links_to_images):
        # TODO catch exceptions
        page_url = urljoin(BASE_URL + 'apod/', image_tag['href'])
        filename = os.path.join(FOLDER, image_tag.text + '.jpg')
        img_url = get_img_url(page_url)
        download_image(img_url, filename)
        if i > 10:
            break


def get_img_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')  # could use lxml -> faster
    img_src = soup.find('img').get('src')
    return urljoin(BASE_URL, img_src)


def download_image(url, filename):
    res = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in res:
            f.write(chunk)


if __name__ == '__main__':
    main()
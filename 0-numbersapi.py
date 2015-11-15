"""Demo of requests package."""

import requests


def main():
    params = {
        'json': ''
    }
    try:
        page = requests.get('http://numbersapi.com/42', params=params)
    except requests.ConnectionError:
        print("Could not establish connection.")
        exit()
    print(page.json()['text'])

if __name__ == '__main__':
    main()

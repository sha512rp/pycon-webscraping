import requests


def upload_palette(username, password, c1, c2, c3, c4, c5):
    login_url = 'https://coolors.co/ajax/login'
    login_data = {
        'e': username,
        'p': password
    }
    session = requests.Session()
    res = session.post(login_url, data=login_data)
    res_json = res.json()
    assert res_json['result'] == 0, "logging in failed"

    palette_url = 'https://coolors.co/ajax/add_user_palette'
    palette_data = {
        "c1": "#" + c1,
        "c2": "#" + c2,
        "c3": "#" + c3,
        "c4": "#" + c4,
        "c5": "#" + c5,
        "name": "__test__",
        "tags": "",
        "key": "Coolors_Simple_KEY"
    }
    res = session.post(palette_url, data=palette_data)
    assert len(res.text), "couldn't save the palette"


if __name__ == '__main__':
    import sys
    sys.argv.pop(0)
    upload_palette(*sys.argv)

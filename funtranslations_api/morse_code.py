import requests

_base_url = "https://api.funtranslations.com/translate/"

def eng_to_morse(text):
    data = dict(text=text)
    print(data)
    translated = requests.post(_base_url+"morse.json").json()
    return translated["contents"]["translated"]
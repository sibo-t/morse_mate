import requests

_base_url = "https://api.funtranslations.com/translate/"

def translate_text_to_morse(text):
    data = dict(text=text)
    translated = requests.post(_base_url+"morse.json",json=data).json()
    return translated["contents"]["translated"]

def translate_morse_to_text(morse_code):
    data = {"text" : morse_code}
    response = requests.post(_base_url+"morse.json",data=data)
    if response.status_code == 200:
        return response.json()["contents"]["translated"]
    return None

import requests

def translate_text(text, target_lang='uk'):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': 'auto',
        'tl': target_lang,
        'dt': 't',
        'q': text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        return translation
    else:
        return "Error: Unable to translate text"

# Використання функції перекладу
text_to_translate = "Hello, world!"
translated_text = translate_text(text_to_translate)
print(translated_text)

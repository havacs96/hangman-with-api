import requests

def get_api_data():
    word_from_api = ""
    response = requests.get("http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
    print(response.json())
    for word_dicts in response.json()[0]:
        word_from_api += word_dicts.get("word")
    print(word_from_api)

get_api_data()
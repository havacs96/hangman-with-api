import requests

def get_api_data():
    word_from_api = ""
    response = requests.get("http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
    for word_dict in response.json():
        #print(response.json())
        word_from_api += word_dict.get("word")
    return word_from_api.lower()


 #TODO Make API trier, to rerun method if it gives API rate limit exceeded error!
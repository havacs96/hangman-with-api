import requests

def get_api_data(api_by_difficulty):
    word_from_api = ""
    for word_dict in api_by_difficulty.json():
        word_from_api += word_dict.get("word")
    return word_from_api.lower()


def get_api_by_difficulty(difficulty):
    if difficulty == 1:
        return requests.get("http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=14&maxLength=25&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
    elif difficulty == 2:
        return requests.get("http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=8&maxLength=14&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
    elif difficulty == 3:
        return requests.get("http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=3&maxLength=8&limit=1&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
 
 #TODO Make API trier, to rerun method if it gives API rate limit exceeded error!
import requests
from abc import ABC,abstractmethod



class Joke(ABC):   

    @abstractmethod
    def get_random_joke(self):
        pass

class JokeAPI(Joke):
       
    def get_random_joke(self):
        result = requests.get('https://v2.jokeapi.dev/joke/Any?lang=de&blacklistFlags=racist,sexist')
        data_json = result.json()
        joke = data_json.get('joke')
        return joke


class DadjokeAPI (Joke):
 
    def get_random_joke(self):
        result = requests.get('https://icanhazdadjoke.com/slack')
        data_json = result.json()
        return data_json['attachments'][0]['text']



class HumorAPI (Joke):
    def __init__(self,**kwargs):
        self.api_token = kwargs.get("api_token")


    def get_random_joke(self):
        params = {'api-key': self.api_token}
        result = requests.get('https://api.humorapi.com/jokes/search', params=params)
        data_json = result.json()
        
        return data_json['jokes'][0]['joke']
       
    




if __name__ == "__main__":
    
    JokeAPI_obj = JokeAPI()
    print( 'First joke: ',JokeAPI_obj.get_random_joke(),'\n')

    DadjokeAPI_obj = DadjokeAPI()
    print('Second joke: ',DadjokeAPI_obj.get_random_joke(), '\n')
    

    HumorAPI_obj = HumorAPI(api_token='fa85ccc2c80a4aa7b196a16352655288')
    print('Third one: ' ,HumorAPI_obj.get_random_joke())

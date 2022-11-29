# Inspire.py - module to grab inspiration quotes from an api  
# aka starting the day right

import requests

class Inspire:
    def __init__(self):
        pass

    def Fetch_Inspiration(self):
        
        #? returns json data from api 
        #TODO: Change api this one is down
        responce  = requests.get("https://motivational-quote-api.herokuapp.com/quotes/random")
        res_dict = responce.json()

        #? grabs value from json data
        quote = res_dict['quote'] 
        author = res_dict['person'] 

        #?returns tuple remember has to be in this order
        return quote , author 


if __name__ == "__main__":
    inspire = Inspire()
    quote , author = inspire.Fetch_Inspiration()
    print(f"Quote: {quote}")
    print(f"Author: {author}")

#works fine can't find anything exactly to add
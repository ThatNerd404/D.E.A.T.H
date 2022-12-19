# Inspire.py - module to grab inspiration quotes from an api  
# aka starting the day right

import requests
import random

class Inspire:
    def __init__(self):
        pass

    def Fetch_Inspiration(self):
        
        #? returns json data from api 
        quote_api  = requests.get("https://type.fit/api/quotes")
        quote_dict = quote_api.json()
        selected_quote = random.choice(quote_dict)
        
        #? grabs value from json data
        quote = selected_quote['text']
        author = selected_quote['author']
        
        #? fixing author when it turns none to something nicer looking
        #? Can be removed if desired
        if author == None:
            author = "Unknown"
            
        #?returns tuple remember has to be in this order
        return quote, author 


if __name__ == "__main__":
    inspire = Inspire()
    quote, author = inspire.Fetch_Inspiration()
    print(quote)
    print(author)
#works fine can't find anything exactly to add
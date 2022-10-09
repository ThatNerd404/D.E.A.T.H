# Inspire.py - module to grab inspiration quotes from an api  

import requests

class Inspire:
    def __init__(self):
        pass

    def Inspiration(self):
        responce  = requests.get("https://motivational-quote-api.herokuapp.com/quotes/random")
        res_dict = responce.json() #? returns dictonary
        quote = res_dict['quote'] 
        author = res_dict['person'] #? stores the value as a string

        return quote , author #?returns tuple

#? How to use |
#?           \_/
if __name__ == "__main__":
    inspire = Inspire()
    quote , author = inspire.Inspiration() #?turns tuple into string
    print(f"Quote: {quote}")
    print(f"Author: {author}")

#works fine can't find anything exactly to add
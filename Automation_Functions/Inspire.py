# Inspire.py - module to grab inspiration quotes from an api  
# aka starting the day right
import requests
class Inspire:
    def __init__(self):
        pass

    def Fetch_Inspiration(self):
        responce  = requests.get("https://motivational-quote-api.herokuapp.com/quotes/random")
        res_dict = responce.json() #? returns dictonary

        quote = res_dict['quote'] 
        author = res_dict['person'] #? stores the value as a string

        return quote , author #?returns tuple remember has to be in this order

#? How to use |
#?           \_/
if __name__ == "__main__":
    inspire = Inspire()
    quote , author = inspire.Fetch_Inspiration() #?turns tuple into string
    print(f"Quote: {quote}")
    print(f"Author: {author}")

#works fine can't find anything exactly to add
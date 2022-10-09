# Inspire.py - module to grab inspiration quotes from an api  

import requests

responce  = requests.get("https://motivational-quote-api.herokuapp.com/quotes/random")
res = responce.json()
quote = res['quote']
author = res['person']

print(f"quote: {quote} author: {author}")
#returns a dict need ot learn how to grab data from dict to print or store
#what i want in a variable 
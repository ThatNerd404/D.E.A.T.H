# Inspire.py - module to grab inspiration quotes from an api  
import bs4
import requests
import json 
responce  = requests.get("https://motivational-quote-api.herokuapp.com/quotes/random")
res = responce.text
'''weathersoup = bs4.BeautifulSoup(res.text, features= "lxml")
temp_element = weathersoup.select('div p ')
temp = str(temp_element[4].get_text())'''

print(res)
#returns a dict need ot learn how to grab data from dict to print or store
#what i want in a variable 
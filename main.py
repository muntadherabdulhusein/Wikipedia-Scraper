import requests
from bs4 import BeautifulSoup

import pandas as pd

import lxml

url="https://country-leaders.onrender.com/"

req= requests.get(url)
status_url ="/status"
req = requests.get(f"{url}/{status_url}")

soup= BeautifulSoup(req.text,"html.parser")


if req.status_code == 200:
   print(req.text)
else :
   print(req.status_code)
cookie_url = "https://country-leaders.onrender.com/cookie"
response = requests.get (cookie_url)
cookies=response.cookies
print(cookies)
countries_url = "https://country-leaders.onrender.com/countries"
countries = requests.get(countries_url,cookies=cookies)
countries_list =countries.json()
print(countries_list)
leaders_url="https://country-leaders.onrender.com/leaders"
leaders = requests.get(leaders_url,cookies=cookies, params={"country":"be"})
leaders_list=leaders.json()
print(leaders_list)
import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

countries_url = "https://country-leaders.onrender.com/countries"
leaders_url="https://country-leaders.onrender.com/leaders"


leaders_per_country = {}

params={"country":""}


for country in countries_list:
    params["country"] = country 

    leader_response = requests.get(leaders_url,cookies=cookies, params= params)


    leaders_per_country[country] = leader_response.json()


#At this point, leaders_per_country contains all the results
print(leaders_per_country)
paragraphs = soup.find_all('p')

#Initialize variable to store the first meaningful paragraph
first_paragraph = None

#Loop through all paragraphs
for paragraph in paragraphs:

    text = paragraph.get_text().strip()

    # Check if the paragraph has meaningful content (adjust the condition as needed)
    if len(text) > 50:  # Minimum length to filter out short/irrelevant paragraphs
        first_paragraph = text
        break  # Exit loop once the first meaningful paragraph is found

#Output the first meaningful paragraph
print(first_paragraph)
#Optionally, filter out paragraphs with no content (e.g., empty strings)
non_empty_paragraphs = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

#Display the paragraphs stored in the variable
print("Extracted Paragraphs:", non_empty_paragraphs)



































































#importing the libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

while True:
    song_year = int(input("Enter a year between 1946-2021: "))
    if song_year < 1946:
        print("Year not available.")
        continue
    elif song_year > 2021:
        print("Year not available.")
        continue
    else:
        break
    

song_year_str = str(song_year)

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_" + song_year_str
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
year=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(year))
# convert list to dataframe
df=pd.DataFrame(df[0])


# drop the unwanted columns
data = df.drop(["Artist(s)", "No.",], axis=1)


songs = df['Title'].values.tolist()

your_random_song = random.choice(songs)

print(your_random_song)
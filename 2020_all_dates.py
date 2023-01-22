import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib import request
import numpy as np
import re


all_data = pd.DataFrame()

for i in range(1,35):
    r = request.urlopen("https://chile.as.com/resultados/futbol/chile/2020/jornada/regular_a_" + str(i) + "/")
    soup = bs(r, 'html.parser')
    table = soup.find_all(["a"], attrs={'class': 'resultado'})
    score_home = []
    score_away = []
    for j in table:
        #print(i.string.split())
        score_result = j.string.split()
        score_home.append(score_result[0])
        score_away.append(score_result[2])
    home = []
    away = []
    for k in table:
        #print(i["title"].split("-"))
        result = k["title"].split("-")
        home.append(result[0])
        away.append(result[1])
    
    match_day = [i]*9

    df = pd.DataFrame(list(zip(match_day, home, score_home, score_away, away)), columns =["match_day", 'home', "score_home", "score_away", "away"]) 
    all_data = pd.concat([all_data, df])

# Cleaning white spaces
#df.columns = df.columns.str.lstrip()

all_data["home"] = all_data["home"].str.lstrip() 
all_data["home"] = all_data["home"].str.rstrip() 

all_data["away"] = all_data["away"].str.lstrip() 
all_data["away"] = all_data["away"].str.rstrip() 

#Checking if all the Scrapping was made correctly
#all_data.loc[all_data["match_day"]==34]

all_data.groupby(["home"]).count()
all_data.groupby(["away"]).count()



all_data.to_csv("all_data.csv", index=False)



   
    
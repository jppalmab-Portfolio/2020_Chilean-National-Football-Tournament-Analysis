import pandas as pd
import numpy as np

# upload the data frame
df = pd.read_csv("./all_data.csv")

df.head(50)

# def some function in order to make new variables with logical conditions

def home_winner(row):
    if row["score_home"] > row["score_away"]:
        return 3
    if row["score_home"] == row["score_away"]:
        return 1
    if row["score_home"] < row["score_away"]:
        return 0

def away_winner(row):
    if row["score_home"] > row["score_away"]:
        return 0
    if row["score_home"] == row["score_away"]:
        return 1
    if row["score_home"] < row["score_away"]:
        return 3

## Use apply method to run the functions above
df["home_points"] = df.apply(lambda row: home_winner(row), axis=1)
df["away_points"] = df.apply(lambda row: away_winner(row), axis=1)


#### MAKE THE NEW DATA FRAME ONLY WITH THE POINTS
home = df[["match_day", "home", "home_points"]]
away = df[["match_day", "away", "away_points"]]

#rename for not have a problems in the future append
home = home.rename(columns = {"home":"club", "home_points":"points"})
away = away.rename(columns = {"away":"club","away_points":"points"})

home.groupby(["club", "points"]).count()
away.groupby(["club", "points"]).count()

#all_points = home.append(away)
all_data = pd.concat([home, away])

all_data = all_data.sort_values(["match_day","club"], ascending=(True,True))

all_data.head(50)

#all_data.groupby(["match_day"]).count()


#########################################
### TRANSFORM THE DATA SET FOR GRAPHING

all_data["cum_sum"] = all_data.groupby(["club"])["points"].cumsum()

all_data.to_csv("all_data_cumsum_long.csv")

df_by_match = all_data.pivot(index="match_day", columns="club")["points"]

df = df_by_match.cumsum()

df_by_match.to_csv("all_data_not_cum.csv", index=False)
df.to_csv("all_data_cum.csv", index=False)

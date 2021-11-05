"""Summary

Attributes:
    contract_ranking (list): Description
    df (TYPE): Description
    per_cols (list): Description
    salary_cols (list): Description
    standardize (TYPE): Description
"""
import os
import re
#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pltly
import plotly.graph_objs as go
from data import SALARY_DATA_20_21, PER_DATA_20_21, TM_DATA_20_21, TM_DATA_17_18


SALARY_DATA = SALARY_DATA_20_21
PER_DATA = PER_DATA_20_21
TM_DATA = TM_DATA_20_21

# create mapping for team names to team abbreviations

team = TM_DATA_17_18['Team']
tm = TM_DATA_17_18['Tm']

import pdb
pdb.set_trace()

team_tm_map = {x.replace('*', ''): y for x, y in zip(team, tm)}


"""
Resources:
https://www.basketball-reference.com/contracts/players.html
https://www.reddit.com/r/nba/comments/6dvmr1/best_advanced_stat_to_measure_how_good_a_player_is/
https://fansided.com/2017/01/31/nylon-calculus-reinventing-per/

Looks like best all in one stats are
PER (Player Efficiency Rating)
WS (Win Shares)
RPM (Real Plus Minus)
BPM (Boxscore Plus Minus)
"""

# get rid of the stuff to the right of \ i.e. LeBron James\jamesle01
standardize = lambda f: f.rsplit('\\')[0].lower()

# function for getting team abbreviation
get_tm_abbreviation = lambda f: team_tm_map[f.replace("*", "")]
# make money a float not a string


def monify(m):
    """Summary

    Args:
        m (string): money string

    Returns:
        float: money value
    """
    try:
        return float(re.sub('[$,]', '', m))
    except:
        return m

SALARY_DATA['Player'] = SALARY_DATA['Player'].map(standardize)
SALARY_DATA['Guaranteed'] = SALARY_DATA['Guaranteed'].map(monify)
PER_DATA['Player'] = PER_DATA['Player'].map(standardize)
TM_DATA['Win Percentage'] = TM_DATA['W'] / (TM_DATA['W'] + TM_DATA['L'])

# add Team abbreviations (they stopped being available in later data pulls)

TM_DATA['Tm'] = TM_DATA['Team'].map(get_tm_abbreviation)


salary_cols = ['Player', 'Tm', 'Signed Using', 'Guaranteed']
per_cols = ['Rank', 'Player', 'PER']
bpm_cols = ['Player', 'BPM']
tm_cols = ['Tm', 'Win Percentage']

df = TM_DATA[tm_cols].merge(
    SALARY_DATA[salary_cols].merge(
        PER_DATA[per_cols],
        on='Player'),
    on='Tm')

print(df)

"""
Visualization
"""

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(6.5, 6.5))


sns.scatterplot(x="PER", y="Guaranteed",
                hue="Tm",
                sizes=(1, 8), linewidth=0,
                data=df, ax=ax)

ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.suptitle("Player Efficiency vs. Guaranteed $\$ by Team")

# plt.show()

tracePER = go.Scatter(x=df['PER'], y=df['Guaranteed'], mode='markers', name='PER',
                      text=df['Player'],
                      marker=dict(
    size=16,
    color=df['Win Percentage'],  # set color equal to a variable
    colorbar=dict(title='Team Win Percentage (%)'),
    colorscale='Viridis',
    showscale=True
))


layout = go.Layout(
    title='Good Contract, Bad Contract',
    xaxis=dict(
        title='Player Efficiency Rating (PER)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Contract Guarantee ($)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=[tracePER], layout=layout)


# data = [tracePER]

pltly.plot(fig)

# pltly.plot([traceBPM])

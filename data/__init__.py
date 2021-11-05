import os
import pandas as pd


SALARY_DATA_17_18 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'salary_contract_player_17_18.csv'))
SALARY_DATA_20_21 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'salary_contract_player_20_21.csv'))

# https://www.basketball-reference.com/leaders/per_active.html
# https://www.basketball-reference.com/leaders/per_career.html
PER_DATA_17_18 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'PER_player_career_regszn_17_18.csv'))
PER_DATA_20_21 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'PER_player_regszn_20_21.csv'))


BPM_DATA_17_18 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'BPM_player_career_regszn_17_18.csv'))


TM_DATA_17_18 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'team_data_17_18.csv'))
TM_DATA_20_21 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'team_data_20_21.csv'))

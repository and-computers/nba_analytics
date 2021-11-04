import os
import pandas as pd

SALARY_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__), 'salary_contract_player_18.csv'))
SALARY_DATA_21_22 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'salary_contract_player_21_22.csv'))
# https://www.basketball-reference.com/leaders/per_active.html
PER_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__), 'PER_player_career_regszn_18.csv'))
BPM_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__), 'BPM_player_career_regszn_18.csv'))
TM_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__), 'team_data_18.csv'))

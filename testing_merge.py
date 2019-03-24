import pandas as pd
pd.read_csv
season_df = pd.read_csv('season_log_10th.csv')
linescores_df = pd.read_csv('linescores_10th.csv')
merged_data = season_df.merge(linescores_df, how='left', on=['GAME_ID', 'TEAM_ABBREVIATION'])
merged_data.to_csv('merged_test.csv')
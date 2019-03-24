import scrapy
import json
import pandas as pd

class NbaStatsLog(scrapy.Spider):
	name = 'nba_seasonlog'
	log_url = 'https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=03%2F10%2F2019&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2018-19&SeasonType=Regular+Season&Sorter=DATE'
	download_delay = 2
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

	def start_requests(self):
		yield scrapy.Request(self.log_url, headers=self.headers)


	def parse(self, response):
		data = json.loads(response.body)
		season_log = data['resultSets'][0]
		season_df = pd.DataFrame(columns=season_log['headers'], data=season_log['rowSet'])
		linescores_df = pd.read_csv('linescores_10th.csv')
		linescores_df['GAME_ID'] = linescores_df['GAME_ID'].astype(str)
		merged_data = season_df.merge(linescores_df, how='outer', on=['GAME_ID', 'TEAM_NAME'])
		merged_data.to_csv('merged_10th.csv')
		
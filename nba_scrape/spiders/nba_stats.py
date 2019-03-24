import scrapy
import json
import pandas as pd

class NbaStatsLog(scrapy.Spider):
	name = 'nbagames'
	games_url = 'https://stats.nba.com/stats/scoreboardv2/?leagueId=00&gameDate=03%2F10%2F2019&dayOffset=0'
	download_delay = 2
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

	def start_requests(self):
		yield scrapy.Request(self.games_url, headers=self.headers)


	def parse(self, response):
		data = json.loads(response.body)
		header = data['resultSets'][0]
		line_score = data['resultSets'][1]
		header_df = pd.DataFrame(columns=header['headers'], data=header['rowSet'])
		header_df.to_csv('day_games_10th.csv')
		linescores_df = pd.DataFrame(columns=line_score['headers'], data=line_score['rowSet'])
		linescores_df.to_csv('linescores_10th.csv')

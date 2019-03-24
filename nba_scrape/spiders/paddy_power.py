import scrapy
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PpOdds(scrapy.Spider):
	name = 'ppodds'
	allowed_domains = ['paddypower.com']
	start_urls = ['https://www.paddypower.com/basketball/nba/']
	download_delay = 2

	def __init__(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('headless')
		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/ben/path_executable/chromedriver')
		self.driver.implicitly_wait(30)


	def parse(self, response):
		self.driver.get(response.url)
		nba_games = self.driver.find_elements_by_class_name('avb-item__scoreboard')
		game_links = [game.get_attribute("href") for game in nba_games]
		for game in game_links:
			self.driver.get(game)
			odds_headers = self.driver.find_elements_by_class_name('accordion__header')
			print(odds_headers)
			# for header in odds_headers:
			# 	time.sleep(3)
			# 	header.click()
			odds = [btn.text for btn in self.driver.find_elements_by_class_name('btn-odds')]
			print(odds)
			odds_file = pd.DataFrame.from_dict(dict(odds))
			odds_file.to_csv('pp_odds.csv')
		self.driver.close()

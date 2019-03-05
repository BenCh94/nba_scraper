import scrapy


class NbaStatsScraper(scrapy.Spider):
    name = "nba_stats"

    def start_requests(self):
        urls = [
            'http://www.espn.com.au/nba/scoreboard/_/date/20190304',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # boxscores = response.selector.css("a").xpath("@href").getall()
        # /a[contains(@class, "button-alt sm")]
        boxscores = response.selector.xpath("//*[@class='button-alt sm']/@href").getall()
        stat_links = [link for link in boxscores]
        # stat_links = response.xpath("//*[@id='401071617']/div/section/a[2]")
        print(stat_links)
        
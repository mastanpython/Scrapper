from autoscraper import AutoScraper

url = 'https://finance.yahoo.com/quote/AAPL/'

wanted_list = ["."]

scraper = AutoScraper()

result = scraper.build(url, wanted_list)
print(result)


url = 'https://www.ndtv.com/'

wanted_list = ['gdg_wdg-btn']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)




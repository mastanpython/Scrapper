import scrapy
import json


class SkymarkSpider(scrapy.Spider):
    name = "skymark"
    allowed_domains = ["www.skymarkinternational.com"]
    start_urls = ["https://www.skymarkinternational.com/"]

    def parse(self, response):
        print("\n")

        allContent = response.css(".sliderbg")

        firstContent = response.css(".sliderbg")
        secondContent = response.css(".product-container")
        thirdContent = response.css(".container")
        
        for item in zip(firstContent,secondContent,thirdContent):
		    #create a dictionary to store the scraped info
            scraped_info = {
                'firstContent' : item[0],
                'secondContent' : item[1],
                'thirdContent' : item[2],
		    }
        
            with open("skymark.json", "w") as filee:
                filee.write('[')

                for index, products in enumerate(response.css('section.product-container')):
                    json.dump({
                        'content': products.css('div.container').extract_first(),
                    }, filee)
                    if index < len(response.css('section.product-container')) - 1:
                        filee.write(',')
                filee.write(']')

            
            yield scraped_info


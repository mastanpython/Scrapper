import scrapy
import json
from bs4 import BeautifulSoup


class SkymarkSpider(scrapy.Spider):
    name = "skymark"
    allowed_domains = ["www.skymarkinternational.com"]
    start_urls = ["https://www.skymarkinternational.com/"]

    # def parse(self, response):
    #     # Define the specific section to include it in the scrape
    #     specific_section = "section"  # Adjust this to target the section tag of interest

    #     # Select the section tag itself if it's not a div, and all direct child tags except divs
    #     # Here, we're including the section itself, and direct children not being div
    #     section_and_tags = response.xpath(f"//{specific_section}[not(self::div)] | //{specific_section}/*[not(self::div)]")

    #     for tag in section_and_tags:
    #         yield {
    #             'tag_name': tag.xpath("name()").get(),
    #             'attributes': tag.attrib,
    #             'text': str(tag)  # Consolidates all text within the tag
    #         }
    #Working
    def parse(self, response):
        #   working
        # Define the specific section to include it in the scrape
        specific_section = "section"  # Adjust this to target the section tag of interest

        # Select the section tag itself if it's not a div, and all child tags except divs
        section_and_tags = response.xpath(f"//{specific_section}[not(self::div)] | //{specific_section}//*[not(self::div)]")

        for tag in section_and_tags:
            tag_name = tag.xpath("name()").get()
            # print(tag)
            tag_data = str(tag)
            yield {
                tag_name: tag_data
                # 'attributes': tag.attrib
                # 'text': ''.join(tag.xpath(".//text()").extract()).strip()  # Consolidates all text within the tag
            }
    # # def parse(self, response):
    #     # Define the specific section within which to look for tags
    #     specific_section = "section"  # Replace with the tag name you want to target

    #     # Extract all tags except <div> tags within the specific section
    #     tags_except_div = response.xpath(f"//{specific_section}//*[not(self::div)]")

    #     for tag in tags_except_div:
    #         # Extract tag name
    #         tag_name = tag.xpath("name()").get()
    #         # print(tag)
    #         tag_data = str(tag)

    #         # Extract tag attributes and text content (if needed)
    #         tag_attributes = tag.attrib
    #         tag_text = tag.xpath("text()").get()

    #         # Yield the extracted information
    #         yield {
    #             f"{tag_name}": tag_data,
    #         }
    # def parse(self, response):
    #     # Extract all tags except <div> and <script> tags
    #     # all_tags_except_div_and_script = response.xpath("//*[not(self::div) and not(self::script)]")
    #     all_tags_except_div_and_script = response.xpath("//*[section]")
    #     # all_tags_except_div_and_script1 = all_tags_except_div_and_script[0].get("//*[not(div)]")
    #     # print(all_tags_except_div_and_script)
    #     print("type==========",type(all_tags_except_div_and_script),len(all_tags_except_div_and_script))
    #     data = all_tags_except_div_and_script.get("data")
    #     print(data)
    #     soup = BeautifulSoup(data, 'html5lib')
    #     all_tags_except_div1 = soup.find_all(lambda tag: tag.name != 'div')
    #     # print("==========all_tags_except_div",all_tags_except_div1)

    #     for tag in all_tags_except_div1:
    #         # Extract tag name
    #         tag_name = tag.name

    #         # Extract tag attributes
    #         tag_attributes = tag.attrs

    #         # Extract text content
    #         # tag_text = tag.get_text()

    #     # print(all_tags_except_div_and_script)

    #     # for tag in all_tags_except_div_and_script:
    #     #     # Extract tag name
    #     #     tag_name = tag.xpath("name()").get()
    #     #     print(tag)

    #         # Extract tag attributes and text content (if needed)
    #         # tag_attributes = tag.attrib
    #         # tag_text = tag.xpath("text()").get()

    #         # Yield the extracted information
    #         # yield {
    #         #     'tag_name': tag_name,
    #         #     'attributes': tag_attributes,
    #         #     'text': tag_text
    #         # }

# class SkymarkSpider(scrapy.Spider):
#     name = "skymark"
#     allowed_domains = ["www.skymarkinternational.com"]
#     start_urls = ["https://www.skymarkinternational.com/"]

#     def parse(self, response):
#         print("\n")

#         allContent = response.css(".sliderbg")

#         firstContent = response.css(".sliderbg")
#         secondContent = response.css(".product-container")
#         thirdContent = response.css(".container")
        
#         for item in zip(firstContent,secondContent,thirdContent):
# 		    #create a dictionary to store the scraped info
#             scraped_info = {
#                 'firstContent' : item[0],
#                 'secondContent' : item[1],
#                 'thirdContent' : item[2],
# 		    }
        
#             with open("skymark.json", "w") as filee:
#                 filee.write('[')
#                 for index, products in enumerate(response.css('div.sliderbg')):
#                     alltags = products.xpath("//*[not(self::div) and not(self::script)]")
#                     for tag in alltags:
#                         # Extract tag name
#                         tag_name = tag.xpath("name()").get()

#                         # Extract tag attributes and text content (if needed)
#                         tag_attributes = tag.attrib
#                         tag_text = tag.xpath("text()").get()
#                         print(tag_name)

#                     json.dump({
#                         # 'content': products.css('div.container').extract_first(),
#                         # 'content': products.xpath("//*[not(self::div)]"),
#                     }, filee)
#                     if index < len(response.css('div.sliderbg')) - 1:
#                         pass
#                     filee.write(',')

#                 for index, products in enumerate(response.css('section.product-container')):
#                     json.dump({
#                         'content': products.css('div.container').extract_first(),
#                     }, filee)
#                     if index < len(response.css('section.product-container')) - 1:
#                         filee.write(',')
#                 filee.write(']')

            
#             yield scraped_info


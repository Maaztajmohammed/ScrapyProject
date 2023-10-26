import scrapy


class BudgetMobilesSpider(scrapy.Spider):
    name = "budget_mobiles"
    allowed_domains = ["noon.com"]
    start_urls = ["https://www.noon.com/uae-en/budget-mobiles/"]

    def parse(self, response):
        mains = response.xpath("//span[@class='sc-37682265-0 diqxXD wrapper productContainer  ']")
        for main in mains:
            name = main.xpath(".//span/span[2]/text()").get()
            new_price = main.xpath(".//strong/text()").get()
            old_price = main.xpath(".//span[@class='oldPrice']/text()[2]").get()
            discount_percent = main.xpath(".//span[@class='discount']/text()").get()
            rating = main.xpath(".//span[@class='sc-dabd6343-1 EPvbo']/text()").get()
            no_of_reviews = main.xpath(".//span[@class='sc-28dcb51c-2 fIFKau']/text()").get()
            url = response.urljoin(main.xpath(".//a/@href").get())
            
            yield {
                'prod_name' : name,
                'old_price' : old_price,
                'new_price' : new_price,
                'discount' : discount_percent,
                'rating' : rating,
                'no_of reviews' : no_of_reviews,
                'url' : url
            }

            


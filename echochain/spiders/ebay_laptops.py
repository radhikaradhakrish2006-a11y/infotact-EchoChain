import scrapy

class EbayLaptopsSpider(scrapy.Spider):
    name = "ebay_laptops"
    allowed_domains = ["ebay.com"]
    start_urls = [
        "https://www.ebay.com/sch/i.html?_nkw=laptop&_sacat=0"
    ]

    def parse(self, response):
        # Each product listing on the search results page
        listings = response.css("li.s-item")

        for item in listings:
            title = item.css("div.s-item__title span::text").get()
            price = item.css("span.s-item__price::text").get()
            condition = item.css("span.SECONDARY_INFO::text").get()
            link = item.css("a.s-item__link::attr(href)").get()

            yield {
                "title": title,
                "price": price,
                "condition": condition,
                "link": link,
            }

        # Handle pagination - go to next page if it exists
        next_page = response.css("a.pagination__next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
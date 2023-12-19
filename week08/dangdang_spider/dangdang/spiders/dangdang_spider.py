import scrapy

class BookSpider(scrapy.Spider):
    name = "dangdang_spider"
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html'] #你可以在这里填写你想爬的当当网图书类别的url

    def parse(self, response):
        for book in response.css('ul.bigimg li'):
            yield {
                'title': book.css('p.name a::attr(title)').extract_first(),
                'price': book.css('p.price span.search_now_price::text').extract_first().replace("&yen;", ""),
                'author': book.css('p.search_book_author span a::text').extract_first(),
                'publisher': book.css('p.search_book_author span a::text').extract()[1],
                'rating' : book.css('p.search_star_line a::text').extract_first()
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
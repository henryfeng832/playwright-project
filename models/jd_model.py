from playwright.sync_api import Page
from csv import DictWriter
from playwright.sync_api import sync_playwright


class JDPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_term_input = page.locator(':nth-match([aria-label="搜索"], 1)')

    def navigate(self):
        self.page.goto("https://www.jd.com/")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")

    def drop_down(self):
        for x in range(1, 12, 2):
            self.page.wait_for_timeout(1000)
            j = x / 9
            js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
            self.page.evaluate(js)

    def wait_load(self):
        self.page.wait_for_load_state('networkidle', timeout=15000)

    def extract_data(self):
        for li in self.page.query_selector_all("#J_goodsList > ul > li"):
            title = li.query_selector(".p-name > a > em").inner_text()
            href = li.query_selector(".p-name > a").get_attribute("href")
            commit = li.query_selector(".p-commit > strong > a").inner_text()
            shop_name = li.query_selector(".p-shop > span > a").inner_text()
            price = li.query_selector(".p-price > strong > i").inner_text()
            icons = [icon.inner_text() for icon in li.query_selector_all(".p-icons > i")]
            _dict = {
                '商品标题': title,
                '商品价格': price,
                '评论数': commit,
                '店铺名字': shop_name,
                '标签': icons,
                '商品详情页': href
            }
            print(_dict)
            self.save_data(_dict)

    def save_data(self, _dict):
        f = open("JD.csv", mode="a", encoding="utf-8", newline=' ')
        csv_writer = DictWriter(f, fieldnames=[
            '商品标题',
            '商品价格',
            '评论数',
            '店铺名字',
            '标签',
            '商品详情页'
        ])
        csv_writer.writer(_dict)


if __name__ == '__main__':
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        search_page = JDPage(page)
        search_page.navigate()
        search_page.search("口红")
        search_page.wait_load()
        search_page.drop_down()
        search_page.wait_load()
        search_page.extract_data()
        browser.close()

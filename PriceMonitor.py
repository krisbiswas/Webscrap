from selenium import webdriver
from time import sleep
from pynotifier import Notification


class PriceFinder:
    price_containers = {"amazon": "//span[contains(@id,'priceblock_ourprice')]", "flipkart": "//div[contains(@class,"
                        "'_1vC4OE _3qQ9m1')]","myntra": "//span[contains(@class,'pdp-price')]"}

    def __init__(self, url):
        sitename = url.split(".")[1]
        if sitename == "amazon":
            self.driver = webdriver.Chrome("C:\\Users\\Krishnandu Biswas\\PycharmProjects\\try_scrap\\chromedriver.exe")
        else:
#             chrome_options = webdriver.ChromeOptions()
#             chrome_options.headless = True
            self.driver = webdriver.Chrome()
        self.driver.get(url)
        print("\t\t Welcome to " + sitename)
        self.driver.set_page_load_timeout(10)
        self.product_price = self.findPrice(sitename)

    def findPrice(self, sitename):
        try:
            price = self.driver.find_element_by_xpath(self.price_containers.get(sitename)).text
            return price
        finally:
            pass
            # self.driver.close()

    def monitor(self):
        sitename = self.driver.current_url.split(".")[1]
        self.driver.execute_script(script="window.location.reload();")
        self.driver.set_page_load_timeout(10)
        currentPrice = self.findPrice(sitename)
        if self.product_price != currentPrice:
            self.product_price = currentPrice
            print(currentPrice)
        print(currentPrice)
            # notifier = Notification()
            # notifier.URGENCY_NORMAL.send()


if __name__ == '__main__':
    url = input("Enter URL to track: ")
    # url = "https://www.amazon.in/Fujifilm-Instax-Mini-Ice-Blue/dp/B06WW64YM6?pd_rd_w=zomAp&pf_rd_p=2be0040d-4b81-4af9-bc32-dce85722aa3c&pf_rd_r=8RPK2YZFR1Q337SXV6KM&pd_rd_r=f9c5d6bd-adbf-49a1-b569-eb6096794d53&pd_rd_wg=kfhB8"
    pf = PriceFinder(url)
    price = pf.product_price
    print("Your product price is: " + price)
    
    # monitor = input("Want to monitor the price? ")
    monitor = "y"
    if monitor.__contains__("y"):
        # interval = input("Give an interval between price check: ")
        interval = 4
        # notification = input("Want notifications on any update? ")
        notification = "n"
        while monitor.__contains__("y"):
            pf.monitor()
            sleep(interval)

    pf.driver.quit()
    
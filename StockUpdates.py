from time import sleep
from selenium import webdriver
import threading


class Stocks:
    def __init__(self):
        # chrome_opt = webdriver.ChromeOptions()
        # chrome_opt.headless = True
        # self.driver = webdriver.Chrome(options=chrome_opt)
        self.driver = webdriver.Chrome()
        self.price = 0

    def find(self, query):
        self.driver.get(url="https://www.google.com")
        sleep(1)
        self.driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys(query + " stock price")
        sleep(1)
        searchScript = 'document.querySelector("input[value=\'Google Search\']").click();'
        self.driver.execute_script(searchScript)
        sleep(2)
        try:
            name = self.driver.find_element_by_class_name("E65Bx").text
            self.price = self.driver.find_element_by_xpath("//span[contains(@class,'IsqQVc NprOob')]").text
            print(name + "\t" + self.price)
        except:
            print("Couldn't find trackable element...")

    # def run(self,comp):
    #     self.monitor(comp)
def monitor(self, company):
    self.find(company)
    while True:
        self.price = self.driver.find_element_by_xpath("//span[contains(@class,'IsqQVc NprOob')]").text
        name = self.driver.find_element_by_class_name("E65Bx").text
        # if master.prices.get(name) != price:
        # print(name + "\t" + self.price)
        sleep(3)

if __name__ == '__main__':
    stockMaster = dict()
    exit = False
    List = list()
    while not exit:
        print("1: Search for Stocks\n2: Monitor a Stock\n3: Add other Stocks\n"
              "4: Get Stock Price by Name\n5: Exit")
        choice = input("Enter your choice: ")
        if int(choice) == 1:
            company = input("Enter Stock Name: ")
            newStock = Stocks()
            newStock.find(company)
            newStock.driver.close()
            del newStock
        if int(choice) == 2:
            company = input("Enter Stock Name: ")
            newStock = Stocks()
            monitor_thread = threading.Thread(name=company, target=monitor(newStock), daemon=True, args=())
            print("jbnlbnlknjk")
            stockMaster.update(company, newStock)
            # monitor_thread.start()
        if int(choice) == 3:
            pass
        if int(choice) == 4:
            company = input("Enter Stock Name for update: ")
            print(stockMaster.get(company).price)
        if int(choice) == 5:
            exit = True

    exit()
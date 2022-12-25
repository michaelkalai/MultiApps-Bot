from selenium import webdriver


class Barber_Finder():
    def echo():
      print("man u ugly")
      url = "https://www.youtube.com/@CoryxKenshin"
      driver = webdriver.Chrome()
      driver.get(url)

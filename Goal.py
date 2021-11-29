from selenium import webdriver
from bs4 import BeautifulSoup

def Goal():
    options = webdriver.ChromeOptions()

    # 창이 뜨지 않게 설정
    options.add_argument('headless')

    path = "C:\\Users\\admin\\Desktop\\SW2\\AD_Project\\chromedriver.exe"  # 크롬 webdriver 설치 경로
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.implicitly_wait(3)  # secondsleague_list = ["epl", "primera", "bundesliga", "seria", "ligue1"]
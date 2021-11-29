from selenium import webdriver
from bs4 import BeautifulSoup
import time


def AttackPointRank(league):
    # 크롬 웹드라이버를 다운받으셔야합니다.
    options = webdriver.ChromeOptions()

    # 창이 뜨지 않게 설정
    options.add_argument('headless')

    path = "C:\\Users\\admin\\Desktop\\SW2\\AD_Project\\chromedriver.exe"  # 크롬 webdriver 설치 경로를 설정해주세요
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.implicitly_wait(3)

    select_league = ""  # 사용자가 선택한 리그

    # 사용자가 선택한 콤보박스 비교
    if league == "EPL":
        select_league = "epl"
    elif league == "Laliga":
        select_league = "primera"
    elif league == "Bundesliga":
        select_league = "bundesliga"
    elif league == "Serie A":
        select_league = "seria"
    elif league == "Ligue 1":
        select_league = "ligue1"

    url = "https://sports.news.naver.com/wfootball/record/index.nhn?category="
    url += select_league + "&tab=player&year=2021"
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="wfootballPlayerRecordBody"]/table/thead/tr/th[5]/a/strong').click()
    time.sleep(0.5)

    page = driver.page_source
    attack_point_rank_box = BeautifulSoup(page, "html.parser")
    attack_point_rank_list = attack_point_rank_box.select('#wfootballPlayerRecordBody>table>tbody>tr')

    rank = ""
    for attack_point in attack_point_rank_list:
        num = attack_point.select('.num > div.inner > strong')[0].text
        name = attack_point.select('.name')[0].text
        rank += num + "위 : " + name + "\n"

    return rank

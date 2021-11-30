from selenium import webdriver
from bs4 import BeautifulSoup


def TeamRank(league):
    # 크롬 웹드라이버를 다운받으셔야합니다.
    options = webdriver.ChromeOptions()

    # 창이 뜨지 않게 설정
    options.add_argument('headless')

    # 크롬 webdriver 설치 경로(절대 경로)를 설정해주세요
    # window version
    # path = "C:\\Users\\admin\\Desktop\\SW2\\AD_Project\\chromedriver.exe"  # 크롬 webdriver 설치 경로를 설정해주세요
    # driver = webdriver.Chrome(path, chrome_options=options)

    # ubuntu version
    path = '/home/seonghwan/workspace/ad_project/chromedriver'
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver.implicitly_wait(3)

    select_league = ''  # 사용자가 선택한 리그

    # 사용자가 선택한 콤보박스 비교
    if league == 'EPL':
        select_league = 'epl'
    elif league == 'Laliga':
        select_league = 'primera'
    elif league == 'Bundesliga':
        select_league = 'bundesliga'
    elif league == 'Serie A':
        select_league = 'seria'
    elif league == 'Ligue 1':
        select_league = 'ligue1'

    url = 'https://sports.news.naver.com/wfootball/record/index.nhn?category='
    url += select_league + '&year=2021'
    driver.get(url)

    page = driver.page_source
    team_rank_box = BeautifulSoup(page, 'html.parser')
    team_rank_list = team_rank_box.select(
        '#wfootballTeamRecordBody>table>tbody>tr')

    rank = ''
    for team in team_rank_list:
        num = team.select('.num > div.inner > strong')[0].text
        name = team.select('.name')[0].text
        rank += num + '위 : ' + name + '\n'

    return rank

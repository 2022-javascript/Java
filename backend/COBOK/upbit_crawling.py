from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
def news_crewling():
    urls = "http://upbit.com/trends"
    driver = webdriver.Chrome('/Users/yuhyeonseog/개인 작업/javascript/study_project/backend/crawling/chromedriver')
    driver.get(urls)
    category_xpath = [
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[1]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[2]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[3]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[4]/a',
        '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[1]/ul/li[5]/a'
    ]
    page_xpath = '//*[@id="UpbitLayout"]/div[3]/div/div[1]/div[3]/div[2]/div/div[2]/a[2]'
    news_name, news_href = [],[]
    category_name = ['전체','일반','규제/정책','산업/테크','칼럼/인터뷰']
    for category,category_name in zip(category_xpath,category_name):
        driver.find_element("xpath",category).click()
        for i in range(5):
            driver.find_element('xpath',page_xpath).click()
            source = driver.page_source
            soup = BeautifulSoup(source,'html.parser')
            news_table = soup.select_one('#UpbitLayout > div:nth-child(4) > div > div.CoinTrend__LeftSide > div:nth-child(3) > div.CoinNews > ul.CoinNews__TitleArticle')
            name_line = []
            href_line = []
            name_line.append(category_name)
            if news_table != None:
                for line in news_table.find_all('a'):
                    name_line.append(line.get_text())
                    href_line.append(line['href'])
                news_name.append(name_line)
                news_href.append(href_line)
    return pd.DataFrame(news_name), pd.DataFrame(news_href)
news_name,news_href = news_crewling()
print(news_name)
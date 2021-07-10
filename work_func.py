import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
def encodejson(link, standard = 'ascii'):
    
    #selenium init
    driver = webdriver.Chrome(executable_path=r'E:/chromedriver_win32/chromedriver.exe')
    
    #startdriver
    driver.get(link)
    content = (driver.page_source).encode(standard, 'ignore')
    driver.quit()

    #beautifulsoup parser
    soup = bs(content)
    pre = soup.find('pre').contents[0]

    #print(pre)
    parsed_json = json.loads(pre)
    return parsed_json

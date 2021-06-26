import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import time

#Autoget Profile ID
# profilename = 'cofight_id'
# profilelink = 'https://www.instagram.com/'+profilename+'/?__a=1'
# getprofileid = requests.get(profilelink) 
# print(getprofileid.status_code) #request status still 429 :(

#selenium init
driver = webdriver.Chrome(executable_path=r'E:/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={%22id%22:%2232679996816%22,%22first%22:50}')
content = (driver.page_source).encode('ascii', 'ignore')
#content = driver.find_element_by_tag_name('pre').text
driver.quit()
# parsed_json = json.loads(content)
# print(parsed_json)
#print(content)

soup = bs(content)
pre = soup.find('pre').contents[0]
#print(pre)
parsed_json = json.loads(pre)

links = []
for each in parsed_json['data']['user']['edge_owner_to_timeline_media']['edges']:
    link = 'https://www.instagram.com'+'/p/'+each['node']['shortcode']+'/'
    posttext = each['node']['edge_media_to_caption']['edges'][0]['node']['text'].replace('\n','')
    comments = each['node']['edge_media_to_comment']['count']
    likes = each['node']['edge_media_preview_like']['count']
    postimage = each['node']['thumbnail_src']
    isvideo = each['node']['is_video']
    postdate = time.strftime('%Y %b %d %H:%M:%S', time.localtime(each['node']['taken_at_timestamp']))
    links.append([link, posttext, comments, likes, postimage, isvideo, postdate])

table = pd.DataFrame(links)
table.columns = ['Link', 'Caption', 'Comments', 'Likes', 'Image Link', 'Video?','Post Date']
print(table)
table.to_csv("cigfhttes.csv")
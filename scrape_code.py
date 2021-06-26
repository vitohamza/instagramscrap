import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

#selenium init
driver = webdriver.Chrome(executable_path=r'E:/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={%22id%22:%2232679996816%22,%22first%22:50}')
content = (driver.page_source).encode('ascii', 'ignore')
driver.quit()

#beautifulsoup parser
soup = bs(content)
pre = soup.find('pre').contents[0]
#print(pre)
parsed_json = json.loads(pre)

#separate json
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

#create dataframe
table = pd.DataFrame(links)
table.columns = ['Link', 'Caption', 'Comments', 'Likes', 'Image Link', 'Video?','Post Date']
print(table)

#convert to csv
table.to_csv("cigfhttes.csv")

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('google API JSON here', scope) #addjsonkey

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Instagram Data Scrap')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

#first row is data header to keep    
sheet_instance.resize(rows=1)
sheet_instance.resize(rows=30)
sheet_instance.insert_rows(table.values.tolist(), row = 2)
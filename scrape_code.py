import work_func
import pandas as pd
import time
from bs4 import BeautifulSoup as bs
#Autoget profile ID
profilename = 'himatektro_its'
#instagramlink = 'https://www.instagram.com/web/search/topsearch/?context=user&count=0&query='+profilename
instagramlink = 'https://www.instagram.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables=%7B%22id%22:%2232679996816%22,%22first%22:50%7D'
ab = work_func.encodejson(instagramlink)
# print(ab)
#beautifulsoup parser
soup = bs(ab)
pre = soup.find('pre').content[0]


#print(pre)
parsed_json = json.loads(pre)
print(parsed_json)

# idjson = getprofile.json()
# idnumber = idjson['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner']['id']

#separate jsons
# links = []
# for each in parsed_json['data']['user']['edge_owner_to_timeline_media']['edges']:
#     link = 'https://www.instagram.com'+'/p/'+each['node']['shortcode']+'/'
#     posttext = each['node']['edge_media_to_caption']['edges'][0]['node']['text'].replace('\n','')
#     comments = each['node']['edge_media_to_comment']['count']
#     likes = each['node']['edge_media_preview_like']['count']
#     postimage = each['node']['thumbnail_src']
#     isvideo = each['node']['is_video']
#     postdate = time.strftime('%Y %b %d %H:%M:%S', time.localtime(each['node']['taken_at_timestamp']))
#     links.append([link, posttext, comments, likes, postimage, isvideo, postdate])

# #create dataframe
# table = pd.DataFrame(links)
# table.columns = ['Link', 'Caption', 'Comments', 'Likes', 'Image Link', 'Video?','Post Date']
# print(table)

# #convert to csv
# table.to_csv("cigfhttes.csv")


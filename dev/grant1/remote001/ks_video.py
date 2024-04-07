import os

import requests
import re

'''headers = {'content': 'application/json',
           'Cookie': 'did=web_96f24dea295ae323eff898f55d7d6f73; kpf=PC_WEB; clientid=3; kpn=KUAISHOU_VISION'
                     'kpn=KUAISHOU_VISION',
           'Host': 'www.kuaishou.com',
           'Origin': 'https://www.kuaishou.com',
           'Referer': 'https://www.kuaishou.com/new-reco',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/119.0.0.0 Safari/537.36 '
           }
for page in range(1, 11):
    json = {
        'operationName': "visionSearchphoto",
        'query': "query visionOttConfig($key: String) {kconf(key: $key)}",
        'variables': "{'keyword':'舞蹈', 'page': 'search', 'pcursor': ''}"
    }
    url = 'https://www.kuaishou.com/graphql'   '''

my_keywords = input("关键字:")
my_save = input("输入保存文件夹路径:",)
my_save_file =my_save.replace('\\', '/')
headers = {
    'content-type': 'application/json',
    'Cookie': 'did=web_96f24dea295ae323eff898f55d7d6f73; kpf=PC_WEB; clientid=3; kpn=KUAISHOU_VISION',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/search/video?searchKey=%E6%B3%B3%E8%A3%85%E5%B0%8F%E5%A7%90%E5%A7%90',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# post请求里面才会有
json = {
    'operationName': "visionSearchPhoto",
    'query': "fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n",
    'variables': {'keyword': "%s" % my_keywords, 'pcursor': '', 'page': "search",
                  'searchSessionId': "MTRfMjcwOTMyMTQ2XzE2NTg5MjM5NDExODBf5rOz6KOF5bCP5aeQ5aeQXzE4NzQ"}
}
url = 'https://www.kuaishou.com/graphql'
response = requests.post(url=url, headers=headers, json=json)
json_data = response.json()
print(json_data)
'''feeds = json_data['data']['visionSearchphoto']['feeds']
for i in range(0, len(feeds)):
    photoUrl = feeds[i]['photo']['photoUrl']
    caption = feeds[i]['photo']['caption']
    print(caption, photoUrl)
    caption = re.sub('[\\/"*?''<>\\n]', '', caption)
    
'''
feeds = json_data['data']['visionSearchPhoto']['feeds']
for i in range(0, len(feeds)):
    photoUrl1 = feeds[i]['photo']['photoUrl']
    caption1 = feeds[i]['photo']['caption']
    print(caption1, photoUrl1)
    caption = re.sub('[\\/:*?"<>|\\n]', '', caption1)
    r = requests.get(photoUrl1, stream=True)
    try:
        with open('%s/%s.mp4' % (my_save_file, caption1), 'wb', ) as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
    except:
        print("部分导出错误")
print("已结束")

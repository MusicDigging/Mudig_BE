import os
import requests

youtube_key = os.environ['YOUTUBE_KEY']
youtube_key1 = os.environ['YOUTUBE_KEY1']
youtube_key2 = os.environ['YOUTUBE_KEY2']
youtube_key3 = os.environ['YOUTUBE_KEY3']
youtube_key4 = os.environ['YOUTUBE_KEY4']
class YouTube:
    def __init__(self, keyword, page, limit):
        self.keyword = keyword
        self.page = page
        self.limit = limit
        
    def youtube(self):
        keyword = self.keyword
        OFFSET = self.page
        LIMIT = self.limit
        # keyword = request.data['keyword']
        # OFFSET  = request.GET.get("page")
        # LIMIT   = int(request.GET.get("limit", 1))
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        keys = [youtube_key, youtube_key1, youtube_key2, youtube_key3, youtube_key4]
        # params = {
        #     'q'             : keyword,
        #     'part'          : 'snippet',
        #     'key'           : youtube_key1,
        #     'regionCode'    : 'KR',
        #     'order'         : 'relevance',
        #     'maxResults'    : LIMIT,
        #     'type'          : 'video',
        #     'pageToken'     : OFFSET
        # }
        # try:
        #     data  = requests.get(search_url, params=params).json()
        #     page  = data['nextPageToken']
        # except KeyError:
        #     params['key'] = youtube_key1
        for key in keys:
            params = {
                'q': keyword,
                'part': 'snippet',
                'key': key,
                'regionCode': 'KR',
                'order': 'viewCount',
                'order': 'relevance',
                'maxResults': LIMIT,
                'type': 'video',
                'pageToken': OFFSET
            }
            try:
                data = requests.get(search_url, params=params).json()
                page = data['nextPageToken']
                print(key)
                break  # 키를 성공적으로 찾았을 때 반복문 종료
            except KeyError:
                continue
        # page = data.get('nextPageToken', None)
        items = data['items']
        result = [
            {
                'link_url'      : 'https://www.youtube.com/embed/'+item['id']['videoId'],
                'title'         : item['snippet']['title'],
                'image_url'     : item['snippet']['thumbnails']['medium']['url'],
                'channel_id'    : item['snippet']['channelId'],
                'channel_title' : item['snippet']['channelTitle'],
                'published_at'  : item['snippet']['publishedAt'],
            } for item in items
        ]
        datas = {
            'message' : result,
            'page' : page,
        }
        return datas
    
    def __str__(self):
        return str(self.__dict__)
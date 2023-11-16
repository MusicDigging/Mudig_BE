import os
import requests

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
        youtube_key = os.environ['YOUTUBE_KEY']
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'q'             : keyword,
            'part'          : 'snippet',
            'key'           : youtube_key,
            'regionCode'    : 'KR',
            'order'         : 'relevance',
            'maxResults'    : LIMIT,
            'type'          : 'video',
            'pageToken'     : OFFSET
        }
        data  = requests.get(search_url, params=params).json()
        page  = data['nextPageToken']
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
    
    # def __str__(self):
    #     return str(self.__dict__)
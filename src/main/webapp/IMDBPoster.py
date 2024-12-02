#IMDBPoster.py
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

def get_poster(movie_id):
    url_template = 'https://www.imdb.com/title/{}'.format(movie_id)
    i = 0
    url = url_template.format(movie_id)
    resp = requests.get(url, headers={'User-agent':'Mozila/5.0'})
    soup = BeautifulSoup(resp.text, features='html.parser')
    poster = soup.select_one('div.ipc-media.ipc-media--poster-27x40.ipc-image-media-ratio--poster-27x40.ipc-media--media-radius.ipc-media--baseAlt.ipc-media--poster-l.ipc-poster__poster-image.ipc-media__img > img')
    return poster.attrs['srcset'][poster.attrs['srcset'].rfind('https'):poster.attrs['srcset'].rfind(' ')]

def get_trailer(movie):
    # YouTube API 키 설정
    api_key = 'AIzaSyBshq4AkCE4L02JCyt_00ux9d4zVi1glAQ'  # API 키를 여기에 입력하세요

    # YouTube API 클라이언트 설정
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 특정 검색어로 검색
    search_query = "{} Official Trailer".format(movie)  # 원하는 검색어로 바꾸세요
    print(movie)
    search_response = youtube.search().list(
        q=search_query,
        part='snippet',
        maxResults=1  # 첫 번째 영상만 불러오기
    ).execute()

    # 첫 번째 검색 결과에서 영상 ID 추출
    video_id = search_response['items'][0]['id']['videoId']

    # 첫 번째 영상의 링크
    iframe = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
    return iframe

print(get_poster('tt0052357'))
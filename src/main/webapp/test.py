from googleapiclient.discovery import build

# YouTube API 키 설정
api_key = 'AIzaSyCETnOTrU6yvCTLFzIAgnUTmo-7dgE232Q'  # API 키를 여기에 입력하세요

# YouTube API 클라이언트 설정
youtube = build('youtube', 'v3', developerKey=api_key)

# 특정 검색어로 검색
search_query = "The Shawshank Redemption Office Trailer"  # 원하는 검색어로 바꾸세요
search_response = youtube.search().list(
    q=search_query,
    part='snippet',
    maxResults=1  # 첫 번째 영상만 불러오기
).execute()

# 첫 번째 검색 결과에서 영상 ID 추출
video_id = search_response['items'][0]['id']['videoId']

# 첫 번째 영상의 링크
iframe = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'

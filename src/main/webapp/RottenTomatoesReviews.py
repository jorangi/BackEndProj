#RottenTomatoesReviews.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
    
def accurate_movie_name(movie_name):
    searching_url = 'https://www.rottentomatoes.com/search?search={}'.format(movie_name)
    resp = requests.get(searching_url)
    soup = BeautifulSoup(resp.text, features='html.parser')
    
    if soup.select_one("search-page-media-row") == None:
        return None
    return soup.select_one("#search-results > search-page-result:nth-child(2) > ul > search-page-media-row:nth-child(1) > a:nth-child(1)").attrs['href'].split("/m/")[1]
def get_movie_audience_reviews(movie_name, top):
    movie_name = accurate_movie_name(movie_name)
    url_template = 'https://www.rottentomatoes.com/m/{}/reviews?type=user'
    name = []
    text = []
    score = []
    i = 0
    url = url_template.format(movie_name)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, features='html.parser')

    if soup.select_one("div.audience-review-row") == None:
        return  None
    for review in soup.select("div.audience-review-row"):
        name.append(review.select_one("div.review-data > div").get_text().replace('\n', '').strip())
        text.append(review.select_one("div.review-text-container > drawer-more > p").get_text().strip())
        score.append(float(review.select_one("div.review-text-container > div.audience-review-meta > rating-stars-group").attrs['score']))
        i+=1
        if i > top-1 :
            break
    d = {
        "name" : name,
        "text" : text,
        "score" : score
    }
    df = pd.DataFrame(data=d)
    return df

def get_movie_critic_reviews(movie_name, top):
    movie_name = accurate_movie_name(movie_name)
    url_template = 'https://www.rottentomatoes.com/m/{}/reviews'
    name = []
    pub = []
    propic = []
    text = []
    score = []
    i = 0
    url = url_template.format(movie_name)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, features='html.parser')

    if soup.select_one("div.review-row") == None:
        return None
    for review in soup.select("div.review-row"):
        name.append(review.select_one("div.review-data a.display-name").get_text().replace("\n", "").strip()),
        pub.append(review.select_one("div.review-data a.publication").get_text().replace("\n", "").strip()),
        propic.append(review.select_one("div.review-data > img").attrs['src'].strip()),
        text.append(review.select_one("div.review-text-container > p:nth-child(1)").get_text().strip()),
        score.append(review.select_one("score-icon-critics").attrs['sentiment'].strip())
        i+=1
        if i > top-1 :
            break
    d = {
        "name" : name,
        "pub" : pub,
        "propic" : propic,
        "text" : text,
        "score" : score
    }
    df = pd.DataFrame(data = d)
    return df

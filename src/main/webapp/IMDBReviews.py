#IMDBReviews.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
import PapagoAPI as pa
    
def get_movie_reviews(movie_id, top):
    url_template = 'https://www.imdb.com/title/{}/reviews/'
    name = []
    text = []
    score = []
    date = []
    link = []
    i = 0
    url = url_template.format(movie_id)
    resp = requests.get(url, headers={'User-agent':'Mozila/5.0'})
    soup = BeautifulSoup(resp.text, features='html.parser')

    if soup.select_one("section.ipc-page-section.ipc-page-section--base.ipc-page-section--sp-pageMargin article") == None:
        return  None
    for review in soup.select("section.ipc-page-section.ipc-page-section--base.ipc-page-section--sp-pageMargin article"):
        if review.select_one('div.ipc-list-card__content > button') != None or review.select_one("span.ipc-rating-star--rating") == None : continue
        name.append(review.select_one("ul a.ipc-link.ipc-link--base").get_text().replace('\n', '').strip())
        t = (review.select_one("h3.ipc-title__text").get_text()+"<**>"+review.select_one('div.ipc-html-content-inner-div').get_text())[0:250]
        if len(t) > 245 : t = t[0:t.rfind(' ')] + "..."
        #print(t)
        #t = pa.translate(t, 'ko')
        text.append(t)
        score.append(review.select_one("span.ipc-rating-star--rating").get_text())
        date.append(review.select_one("ul li.ipc-inline-list__item.review-date").get_text().strip())
        link.append("https://imdb.com/"+review.select_one("a.ipc-title-link-wrapper").attrs['href'])
        i+=1
        if i > top-1 :
            break
    d = {
        "name" : name,
        "text" : text,
        "score" : score,
        "date" : date,
        "link" : link
    }
    df = pd.DataFrame(data=d)
    return df
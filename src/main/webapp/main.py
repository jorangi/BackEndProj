import RottenTomatoesReviews as rt
import PapagoAPI as pa
import pandas as pd
import kagglehub
import SendToSQL as ssql
import IMDBReviews as ir
import IMDBPoster as media

def main():
    path = kagglehub.dataset_download("octopusteam/full-imdb-dataset")
    data = pd.read_csv(path+"/data.csv").dropna()
    
    data['weight'] = ((data['numVotes'] * data['averageRating'] + 25000 * 7.0)/(data['numVotes'] + 25000))
    data['W'] = data['weight'].round(1)
    data['rank'] = data.query('type=="movie"')['weight'].rank(method='first', ascending=False)
    data = data.set_index('rank').dropna()
    data = data.sort_values('rank')
    i = 0
    for index, movie in data.iterrows():
        ssql.update_tbl(media.get_poster(movie['id']), media.get_trailer(movie['title']), movie['id'])
        i+=1
        if(i > 99) : break
    
    # reviews = None
    # i = 0
    # for index, movie in data.iterrows():
    #     print(movie['title'])
    #     rev = ir.get_movie_reviews(movie['id'], 5)
    #     rev['movieTitle'] = movie['title']
    #     rev['movieId'] = movie['id']
    #     rev['id'] = movie['id']+'_'+i
    #     rev['title'] = rev['text'][0:str(rev['text']).find('<**>')]
    #     rev['text'] = rev['text'][str(rev['text']).find('<**>')+4:]
    #     reviews = pd.concat([reviews, rev], ignore_index=True)
    #     i+=1
    #     if(i > maxCount-1) : break
    #ssql.make_tbl(reviews, 'root', '12345678', '3306', 'BPDP', 'reviewTbl')
    #ssql.make_tbl(data.head(1), 'root', '12345678', '3306', 'BPDB', 'movieTbl')
    # ssql.make_tbl(critics, 'root', '12345678', '3306', 'BPDP', 'critReviewTbl')
    
if __name__ == '__main__':
	main()
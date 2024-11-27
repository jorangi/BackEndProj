import RottenTomatoesReviews as rt
import PapagoAPI as pa
import pandas as pd
import kagglehub
import SendToSQL as ssql
import IMDBReviews as ir

def main():
    start = 0
    maxCount = 100 #count - 1
    
    path = kagglehub.dataset_download("octopusteam/full-imdb-dataset")
    data = pd.read_csv(path+"/data.csv").dropna()
    
    data['weight'] = ((data['numVotes'] * data['averageRating'] + 25000 * 7.0)/(data['numVotes'] + 25000))
    data['W'] = data['weight'].round(1)
    data['rank'] = data.query('type=="movie"')['weight'].rank(method='first', ascending=False)
    data = data.set_index('rank').dropna()
    data = data.sort_values('rank')
    data = data.iloc[start:start+maxCount]
    # reviews = None
    # i = 0
    # for index, movie in data.iterrows():
    #     print(movie['title'])
    #     rev = ir.get_movie_reviews(movie['id'], 5)
    #     rev['title'] = movie['title']
    #     rev['id'] = movie['id']
    #     reviews = pd.concat([reviews, rev], ignore_index=True)
    #     i+=1
    #     if(i > maxCount-1) : break
    #ssql.make_tbl(reviews, 'root', '12345678', '3306', 'BPDP', 'reviewTbl')
    ssql.make_tbl(data.head(100), 'root', '12345678', '3306', 'BPDP', 'movieTbl')
    # ssql.make_tbl(critics, 'root', '12345678', '3306', 'BPDP', 'critReviewTbl')
    
if __name__ == '__main__':
	main()
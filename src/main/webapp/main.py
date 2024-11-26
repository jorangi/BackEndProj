import RottenTomatoesReviews as rt
import PapagoAPI as pa
import pandas as pd
import kagglehub


def main():
    path = kagglehub.dataset_download("octopusteam/full-imdb-dataset")
    data = pd.read_csv(path+"/data.csv").dropna()
    
    data['weight'] = ((data['numVotes'] * data['averageRating'] + 25000 * 7.0)/(data['numVotes'] + 25000))
    data['W'] = data['weight'].round(1)
    data['rank'] = data.query('type=="movie"')['weight'].rank(method='first', ascending=False)
    data = data.set_index('rank').dropna()
    data = data.sort_values('rank')
    data.head(10)
    
    datacsv = None
    
    for title in data.head(5)['title']:
        d =rt.get_movie_audience_reviews(title, 3)
        d['movieName'] = title
        datacsv = pd.concat([datacsv, d], ignore_index=True)
        datacsv.to_csv('./test.csv')
        #pd.DataFrame(datacsv).to_csv('test.csv')
        # print(title)
        # print("="*20)
        # print(rt.get_movie_audience_reviews(title, 3))
        # print("="*40)
    print(datacsv)
    #df = rt.get_movie_critic_reviews('parasite', 2)
    #for i in range(len(df)):
    #    df.loc[i, 'text'] = pa.translate(df.iloc[i]['text'])
    #    
    #print(df)
	
	
if __name__ == '__main__':
	main()
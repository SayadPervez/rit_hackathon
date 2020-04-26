from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob
from datetime import datetime,timedelta
import imagextraction

def sentiment(news,value):
    newsfeed = []
    for i in news['articles']:
        article = TextBlob(i['description'])
        if(article.sentiment.polarity >= value):
            t = imagextraction.imgextract(i['title'][:20])
            newsfeed.append([i['source']['name'],i['title'],i['description'],str(t)])
    #returns newssource, title, description and image          
    return newsfeed

#15 day news feed

today = datetime.utcnow().date()
duration = datetime.utcnow().date() - timedelta(days = 15)

#API KEY

news = NewsApiClient(api_key = "0de6787ea7e44a8691ce4a5d556d18dc")

#News extraction

top_headlines = news.get_everything(q='covid OR corona OR success OR recovered OR lockdown OR quarantine OR recovery NOT positive NOT Deadlier NOT Dead',
                                      from_param=duration,
                                      language='en')

#sentiment analysis using Textblob

newsfeed = sentiment(top_headlines,0.2)


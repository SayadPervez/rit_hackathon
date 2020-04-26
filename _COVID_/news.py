from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob
from datetime import datetime,timedelta
import os

def display(newsfeed):
    for i in newsfeed:
        print("\n".join(i))
    print("\n") 

def sentiment(news,value):
    #newsfile = open('newsfile.txt','w')
    newsfeed = []
    for i in news['articles']:
        article = TextBlob(i['description'])
        if(article.sentiment.polarity > value):
            newsfeed.append(i)
            #newsfeed.append([i['source']['name'],i['title'],i['description']])
            #[i['publishedAt']
            """print(i['source']['name'])
            print(i['title'])
            print(i['description'])
            rint("---------------------------------------------------")
            newsfile.write(i['source']['name'])
            newsfile.write("\n")
            newsfile.write(i['title'])
            newsfile.write("\n")
            newsfile.write(i['description'])
            newsfile.write("\n")
            newsfile.write("---------------------------------------------------\n")"""
            
    #returns newssource, title, and description       
    return newsfeed

    #newsfile.close()

def newssources():
    s = []
    #fs = open('sources.txt','w')
    sources = news.get_sources()
    for source in sources['sources']:
        #fs.write(source['name'])
        #fs.write('\n')
        s.append(source['name'])
    #fs.close()
    return s

#15 day news feed

today = datetime.utcnow().date()
duration = datetime.utcnow().date() - timedelta(days = 10)

#API KEY

news = NewsApiClient(api_key = "0de6787ea7e44a8691ce4a5d556d18dc")

#News Sources

#sources = newssources()

#News extraction

top_headlines = news.get_everything(q='covid OR corona OR success OR recovered OR lockdown OR quarantine OR recovery',
                                      from_param=duration,
                                      language='en')
"""url = ('http://newsapi.org/v2/everything?'
       'q=corona&covid'
       'from=2020-04-24&'
       'sortBy=popularity&'
       'apiKey=0de6787ea7e44a8691ce4a5d556d18dc')
top_headlines = requests.get(url)"""

#sentiment analysis using Textblob

newsfeed = sentiment(top_headlines,0.2)

#display(newsfeed)
#print(newsfeed)

tfile="P:\\Pvz_Program_Files\\Web_Development\\COVID\\fdata.txt"
with open(tfile,'w') as d:
    d.write('')
# emptied the file above

def getImg(title):
    os.chdir('P:\\Pvz_Program_Files\\Web_Development\\COVID\\Python Scripts')
    os.system(f'python imagextraction.py "{title}"')
    with open("P:\\Pvz_Program_Files\\Web_Development\\COVID\\Python Scripts\\img.txt",'r') as r:
        x=r.readline()
        return(x)


li=[]
for _ in newsfeed:
    a=str(_['title'])+"`"+str(_['description'])+"`"+str(_['url'])+"\n"
    li.append(a)
li=list(set(li))
a=""
for _ in li:
    a+=_
a=''.join([x for x in a if((ord(x) in range(65,91)) or (ord(x) in range(97,123)) or (ord(x) in range(48,58)) or (ord(x) in [95,58,47,10,96,45,43,42,47,46,61,32,64,38,33,35,36,37,94,38,40,91,93]))])
with open(tfile,'a') as f:    
    f.write(a[:-1])

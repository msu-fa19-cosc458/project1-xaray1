import flask, random
import os, tweepy
import requests, json
                
url = "https://api.genius.com/search?q=Kendrick%20Lamar"
    
my_header = {
    "Authorization": "Bearer FAgfzFh7SC0OjSo3f1W-tsr4UkaanvH5mrXEx_Ay3i9ZXrZcxt2df5bRDzxrDDnX"
}

oauth = tweepy.OAuthHandler(
    "RMYP8WqHLa8TFlRaeqL9x23C8",
    "KAZt85Y2G1cYyeykMWh1t5FlHxlLg8NpweCZABlnDQu7Q9N22F"
    )
oauth.set_access_token(
    "1166769097947918337-3lyxumne3ePs0RpvYtoFOJS95WGjgn",
    "VaSbrKKCzGITwO7sp7abjnRQFvulugbsjUyV9ULiE4wQv"
    ) 
    
api = tweepy.API(oauth)
response = requests.get(url, headers=my_header)
info = response.json()
genius_hits = info["response"]["hits"]
ranint = random.randint(0,len(genius_hits)-1)
song = genius_hits[ranint]
print(song["result"]["header_image_url"])
#print(song["image_url"])

    
def grabTweets():
    cnt = 0
    for tweet in api.search("@father"):
        print(tweet.text)
        cnt += 1
        if cnt == 10:
            break
    return None
    
def grabArt():
    return None

app = flask.Flask(__name__)

@app.route('/Father')
def render(): 
    grabTweets()
    return flask.render_template("structure.html",image = song["result"]["header_image_url"])
    
app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP', '0.0.0.0')
    )
    


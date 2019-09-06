import flask, random
import os, tweepy
import requests, json

app = flask.Flask(__name__)

url = "https://api.genius.com/search?q=Kid%20Cudi"
artisturl = "https://genius.com/artists/KidCudi"
    
my_header = {
    "Authorization": os.getenv("Authorization")
}

oauth = tweepy.OAuthHandler(
    os.getenv("APIKEY"),
    os.getenv("APISECRET")
    )
oauth.set_access_token(
    os.getenv("ACCESSTOKEN"),
    os.getenv("ACCESSKEY")
    ) 
    
api = tweepy.API(oauth)
response = requests.get(url, headers=my_header)

def randomize():
    info = response.json()
    genius_hits = info["response"]["hits"]
    ranint = random.randint(0,len(genius_hits)-1)
    song = genius_hits[ranint]
    return song


def grabTweets():
    tweetset = set()
    x = api.search("@KidCudi")
    for tweet in range(0,9):
        tweetset.add(random.choice(x).text)
    return list(tweetset)
    
def grabImage(song):
    image = song["result"]["header_image_url"]
    return image

def grabSong(song):
    song_name = song["result"]["title"]
    return song_name

@app.route('/')
def render(): 
    song = randomize()
    return flask.render_template("structure.html",image = grabImage(song),
    tweetset = grabTweets(),artisturl = "https://genius.com/artists/KidCudi",song_name = grabSong(song))
    
app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP', '0.0.0.0')
    )
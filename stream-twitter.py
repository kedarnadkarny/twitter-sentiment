from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import json
import time
from threading import Thread as thread

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

consumer_key = "YOUR_CUSTOMER_KEY"
consumer_secret="YOUR_CONSUMER_SECRET"
access_token="YOUR_ACCESS_TOKEN"
access_token_secret="YOUR_ACCESS_TOKEN_SECRET"

def animate(i):
	graph_data = open('twitterDB.csv','r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	i = 0
	total = 0
	for line in lines:
		x = line
		print(x)
		if len(x) > 1:
			xs.append(total)
			ys.append(x)
			total = total + float(x)
			i = i + 1
	ax1.clear()
	ax1.plot(xs, ys)

class listener(StreamListener):
    def on_data(self, raw_data):
        tweet = json.loads(raw_data)
        analysis = TextBlob(tweet['text'])
        print(analysis.sentiment[0])
        saveFile = open('twitterDB.csv', 'a')
        saveFile.write(str(analysis.sentiment[0]))
        saveFile.write('\n')
        saveFile.close()
        return True

    def on_error(self, status_code):
        print(status_code)


def runAnimate():
	print("STARTING RUN ANIMATE")
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

def invokeTwitter():	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=['Clinton'])

t1 = thread(target=invokeTwitter)
t2 = thread(target=runAnimate)
#t2.start()
t1.start()

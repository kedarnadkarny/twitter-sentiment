# twitter-sentiment
Read tweets using Twitter API, understand sentiment using NLP and plot a graph

Version 1
Setup instructions
1. Clone repository
2. Download tweepy, textblob, matplotlib dependencies for Python3.5
3. run stream-twitter.py first
4. run liveplot.py

The textblob library calculates the sentiment of a tweet on a basis of -1 to 1. -1 being negative and 1 being positive
The total is calculated and drawn on the graph with the help of matplotlib

NOTE:
I am still working on this application.
One fix would be using threading to listen the tweets and draw the graph simultaneously
I am facing some issues with matplotlib. I suspect it does not run with threading
If you can suggest me correction, I will be happy to include your name in the project contribution

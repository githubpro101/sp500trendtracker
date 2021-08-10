# sp500trendtracker (replicate the experiment on the relationship between trade volume to media exposure)

original study article - https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0040014&fbclid=IwAR1zisbynNILtRLcJEMdUSj8crPNGZyYq48_JemjJN5UTH-Dvdgfb0pGR5I

"query volumes tend to anticipate trading volumes. Such an anticipation spans from  to  days at most."


trends.py - create trends report through google trends
heavily modified from original https://www.youtube.com/watch?v=cuTUbPQk2R4
pulls SP500 tickers form sp500.py


sp500.py - stock info from yahoo finance
from https://www.youtube.com/watch?v=CaB3o_PbTJU


volume.py - gives historical stock information from yahoo finance API, pulls SP500 tickers from same source as SP500.py
inspriation from https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836


pip install pytrends,yahoo-fin,pandas,lxml

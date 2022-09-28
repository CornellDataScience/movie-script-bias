import numpy as np
from textblob import TextBlob
import json
import pandas as pd
# import movie_script_parser

# pre processing of script into text format
#identify female character's lines vs male character's lines
#run TextBlob on each line, perform binning on each line and sum scores for each 'bin'
#figure out how to identify variety

with open('movie-scripts/legally-blonde-script.json') as f:
   data = json.load(f)

script = []
for line in data['movie_script']:
  if line['type']=='speech':
    #add gender classifier here
    script = script + [line['text']]


sentiments = []
for d in script:
  dialogue = TextBlob(d)
  sentiment = dialogue.sentiment
  sentiments = sentiments + [sentiment]

bins = pd.cut(sentiments,5)
print(bins)
import numpy as np
from textblob import TextBlob
import json
import pandas as pd
# import movie_script_parser

# pre processing of script into text format
#identify female character's lines vs male character's lines
#run TextBlob on each line, perform binning on each line and sum scores for each 'bin'
#figure out how to identify variety

with open('legally-blonde-script.json') as f:
   data = json.load(f)

script = []
for line in data['movie_script']:
  # print(line)
  if line['type']=='speech':
    #add gender classifier here
    script = script + [line['text']]

# print(script)

sentiments = []
for d in script:
  dialogue = TextBlob(d)
  sentiment = dialogue.sentiment
  sentiments = sentiments + [sentiment]

bins = pd.cut(sentiments,5)
print(bins)


# with open("legally-blonde-script) as script:
#   for line in script:
#     print(line.type)
#     dialogue = TextBlob(line.strip())
#     print()
#     # print(dialogue.words[0][1])
#     # if ( not (len(dialogue.words)==1 and dialogue.words[0][1]=='NNP')):
#     print(dialogue)
#     sentiment = dialogue.sentiment
#     sentiments = sentiments + [sentiment]
#     print(sentiment)
# print(pd.cut(sentiments, 5))




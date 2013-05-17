import json, sys

sentiments = {}
state_sentiments = {}
state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def build_sentiment_dict(sent_file):
  for line in sent_file.readlines():
    sentiment, score = line.split("\t")
    sentiments[sentiment] = float(score)

def main():
  # Get arguments
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  datalines = tweet_file.readlines()
  build_sentiment_dict(sent_file)

  # Convert the data line into json.
  tweets = map(lambda tweet: json.loads(tweet.encode('utf-8', 'ignore')), datalines)

  # Print for debugging.
  #print "Tweet text : ", tweets[113]["text"]
  #print "Total number of sentiments : ", len(sentiments)

  # Score each tweet and parse out the city.
  for tweet in tweets:
    if "place" and "text" in tweet:
      if tweet["place"] is not None:
        if(tweet["place"]["country"] == "United States"):
          words = tweet["text"].split()
          tweet_sentiment = sum(map(lambda word: sentiments.get(word, 0.0), words))
          tweet_state = tweet["place"]["full_name"][-2:]
          if tweet_state in state_codes:
            state_sentiments[tweet_state] = state_sentiments.get(tweet_state, 0.0) + 1

  # List out all the states, and print the state with max sentiments.
  #for state, sentiment in state_sentiments.items():
    #print state, sentiment

  happy_state = sorted(state_sentiments.items(), key=lambda x: x[1], reverse=True)[0][0]
  print happy_state

if __name__ == "__main__":
    main()

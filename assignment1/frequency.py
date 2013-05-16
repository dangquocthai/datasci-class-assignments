import sys, json


def main():
  # Get arguments
  tweet_file = open(sys.argv[1])
  # Read with utf-8 encoding
  tweets = tweet_file.readlines()
  tweets = map(lambda tweet: tweet.encode('utf-8', 'ignore'), tweets)
  # Print basic stats for debugging
  print "Total tweets read : " + str(len(tweets))
  print "---Sample Tweet---"
  print json.loads(tweets[103])["text"]

  # Read all tweets and score them.
  scores = {}
  for line in tweets:
      tweet = json.loads(line)
      if "text" in tweet: 
        for word in tweet["text"].split():
          scores[word] = scores.get(word, 0.0) + 1.0

  total_words = sum(scores.values())

  # Print some de-bug.
  print "Total words : ", len(scores.keys())
  print "Total words count : ", total_words

  # Print terms and frequency
  for term, count in scores.items():
      frequency = (count / total_words)
      print term + " " + str(frequency)

if __name__ == "__main__":
    main()

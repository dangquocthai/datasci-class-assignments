import sys, json


def main():
  # Get arguments
  tweet_file = open(sys.argv[1])
  # Read with utf-8 encoding
  tweets = tweet_file.readlines()
  tweets = map(lambda tweet: tweet.encode('utf-8', 'ignore'), tweets)
  # Print basic stats for debugging
  #print "Total tweets read : " + str(len(tweets))
  #print "---Sample Tweet---"
  #print json.loads(tweets[103])["text"]

  hashtags = {}
  for line in tweets:
    tweet = json.loads(line)
    if "entities" in tweet:
      for ht in tweet["entities"]["hashtags"]:
        hashtag = ht["text"]
        hashtags[hashtag] = hashtags.get(hashtag, 0.0) + 1.0

  # Print status
  #print "Total hashtags : ", len(hashtags.keys())

  top_ten_tags = sorted(hashtags.iteritems(), key=lambda x: x[1], reverse=True)[:10]

  for tag, count in top_ten_tags:
    print tag.encode('utf-8', 'ignore'), count

if __name__ == "__main__":
    main()

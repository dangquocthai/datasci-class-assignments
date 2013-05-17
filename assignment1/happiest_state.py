import json, sys

def score_tweet(tweet_line):


def main():
  # Get arguments
  tweet_file = open(sys.argv[1])
  datalines = tweet_file.readlines()

  # Convert the data line into json.
  tweets = map(lambda tweet: json.loads(tweet.encode('utf-8', 'ignore')), datalines)
  #print "Total number of tweets : ", len(tweets)

  list_of_state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

if __name__ == "__main__":
    main()

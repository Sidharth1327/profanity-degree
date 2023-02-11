import re
def profanity_degree(tweet, slurs):
  profanity_words = re.findall(r'\w+' , tweet.lower())
  # usage of regular expression to extract individual words from the tweet
  return sum(word in slurs for word in profanity_words)
def read_tweets(tweets_file):
  with open(tweets_file,'r') as t:
    return t.readlines()
def main():
  slurs = set(["arse","arsehead", "arsehole","nigger","slut","bitch","cunt","nigga","towelhead","bastard","piss","twat"])
  # this slurs are some of them found in google
  tweets = read_tweets("tweets.txt")
  # tweets.text contain one tweet per line
  for tweet in tweets:
    profanity_level = profanity_degree(tweet, slurs)
    if profanity_level == 0:
      print(f"{tweet} => Appropriate")
    elif profanity_level <= 2:
      print(f"{tweet} => Tolerable")
    elif profanity_level <= 4:
      print(f"{tweet} => Moderately Profane")
    else:
      print(f"{tweet} => Offensive")
      
if __name__ == "__main__":
  main()
      
# Assumptions : assumes racial slurs in the list all are lower case.
# degree of profanity is based on number of slur wors in a single tweet

import os
import tweepy as tw
import pandas as pd
import argparse
import requests
import json
import csv


# Accept arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', type = str, required = True)
parser.add_argument('-s', type = str, required = True)
args = parser.parse_args()

output_file = args.o
sub = args.s.replace('/r/', '')

# Define keys
consumer_key = "lVbAr1WjVJZmMnZfqBdElZ6Fe"
consumer_secret = "RqNh1fnrN4hSMuGlkeUdQaOHsedqcFLFKS10j6pdNtJZ5UoMOE"
access_token = "1259296847006437382-QyBmbzIiuv76iY4m89w68WokKtpITz"
access_token_secret = "M7Yr2z6fHVnnFEEdZFuAVA8qpjiUUXMz8mNtTeNGgVwrx"

# Set up tweet collector
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define search terms
search_words = "#ubereats"
date_since = "2022-11-16"


def main():
    # Collect tweets
    tweets = tw.Cursor(api.search_tweets, q=f'{search_words} -filter:retweets', lang = "en", since=date_since).items(200)

    # Iterate and print tweets
    for tweet in tweets:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            print(tweet.text)


if __name__ == '__main__':
    main()
import cohere
from cohere.classify import Example
import requests
import more_itertools
import os
from dotenv import load_dotenv
import pandas as ps

# python-analysis-bot/app.py
load_dotenv()
co = cohere.Client("Mh5kOwSIA4mFHW2Ih1bjJMolh7uANVc1SeG7HKrD")

twitter_api_url = "https://api.twitter.com/2/tweets/search/recent"
twitter_headers = {
   "Authorization": "Bearer {}".format("AAAAAAAAAAAAAAAAAAAAAMsClgEAAAAA1tSoFXgVdZP%2FzvSq4MPM0WjyylI%3Dc2QCCvEe0S01PL9rrLMFphhI8ZYj29HRRs3ZkjazOAkHyU59BV")
}

request_params = {
   'query': '(Uber Eats OR Radish Delivery) lang:en',
   'max_results': 100,
}

#^ dont change
class AnalysisBot():
   retrieved_tweets = []
   classified_tweets = []
   results = {
       'react': {
           'positive': 0,
           'mentions': 0
       },
       'next': {
           'positive': 0,
           'mentions': 0
       },
       'angular': {
           'positive': 0,
           'mentions': 0
       },
       'vue': {
           'positive': 0,
           'mentions': 0
       },
       'node': {
           'positive': 0,
           'mentions': 0
       },
       'ember': {
           'positive': 0,
           'mentions': 0
       }
   }

   def __init__(self) -> None:
       fetch_count = 0

       while (fetch_count < 10):
           print(
               'FETCHING BATCH: #{}. {} tweets retrieved.'
               .format(fetch_count, len(self.retrieved_tweets))
           )

           tweets = requests.request(
               "GET",
               url=twitter_api_url,
               headers=twitter_headers,
               params=request_params
           ).json()

           #print(tweets)
           token = tweets['meta']['next_token']

           if (token):
               request_params["next_token"] = token

           for item in tweets['data']:
               self.retrieved_tweets.append(item['text'])

           fetch_count = fetch_count + 1


   def determine_results(self, framework, classification):
       if (framework in classification.input):
            self.results[framework]['mentions'] = self.results[framework]['mentions'] + 1

            if (classification.prediction == "positive review"):
                self.results[framework]['positive'] = self.results[framework]['positive'] + 1

   def classify_tweets(self):

       tweet_items = list(more_itertools.chunked(self.retrieved_tweets, 10))

       for idx, tweets in enumerate(tweet_items):
           print("PROCESSING:", idx)
           response = co.classify(
               model='large',
               #taskDescription='Classify tweets on Uber Eats delivery people retrieved from the Twitter V2 Search API',
               #outputIndicator='Classify retrieved tweets to determine drivers stance on Uber Eats',
               inputs=tweets,
               examples=[

                   # positive tweets about frameworks
                   Example("Uber eats lets me make a lot of money on my own schedule. Best company ever!", "positive review"),
                   Example(
                       "I love uber eats, I am so happy I can spend time with my kids now.",
                       "positive review"),
                   Example(
                       "By gods grace Uber eats made love again. I met my wife doing a delivery",
                       "positive review"),

                   # negative tweets about frameworks
                   Example(
                       "I dont even break even driving for uber eats. Uber eats is a scam",
                       "negative review"),
                   Example(
                       "Uber causes so much pollution. Its terrible",
                       "negative review"),

                   # neutral tweets about frameworks
                   Example(
                       "I ate my customers order while driving for uber eats lol",
                       "neutral review"),
                   Example("Its a nice sunset that im looking at while driving for uber eats", "neutral review"),
                   Example("got my uber eats salary this week",
                           "neutral review")
               ]
           )

           for classification in response.classifications:
               self.determine_results('react', classification)
               self.determine_results('next', classification)
               self.determine_results('vue', classification)
               self.determine_results('angular', classification)
               self.determine_results('node', classification)
               self.determine_results('ember', classification)

       print("RESULTS:", self.results)


# class AnalysisBot():
#     retrieved_tweets = []
#     classified_tweets = []
#     results = {
#        'react': {
#            'positive': 0,
#            'mentions': 0
#        },
#        'next': {
#            'positive': 0,
#            'mentions': 0
#        },
#        'angular': {
#            'positive': 0,
#            'mentions': 0
#        },
#        'vue': {
#            'positive': 0,
#            'mentions': 0
#        },
#        'node': {
#            'positive': 0,
#            'mentions': 0
#        },
#        'ember': {
#            'positive': 0,
#            'mentions': 0
#        }
#     }
#
#      def __init__(self) -> None:
#            fetch_count = 0
#
#            while (fetch_count < 100):
#                print(
#                    'FETCHING BATCH: #{}. {} tweets retrieved.'
#                    .format(fetch_count, len(self.retrieved_tweets))
#                )
#
#                tweets = requests.request(
#                    "GET",
#                    url=twitter_api_url,
#                    headers=twitter_headers,
#                    params=request_params
#                ).json()
#
#                token = tweets['meta']['next_token']
#
#                if (token):
#                    request_params["next_token"] = token
#
#                for item in tweets['data']:
#                    self.retrieved_tweets.append(item['text'])
#
#                fetch_count = fetch_count + 1
#
#
#
#     def classify_tweets(self):
#         tweet_items = list(more_itertools.chunked(self.retrieved_tweets, 32))
#
#         for idx, tweets in enumerate(tweet_items):
#             print("PROCESSING:", idx)
#             response = co.classify(
#                 model='medium',
#                 taskDescription='Classify tweets on Uber Eats retrieved from the Twitter V2 Search API',
#                 outputIndicator='Classify retrieved tweets to determine employees stance on Uber Eats practices',
#                 inputs=tweets,
#                 examples=[
#                     # positive tweets about frameworks
#                     Example("Uber eats helped me to make money", "positive review"),
#                     Example(
#                         "Uber eats is a great company to work for. I will work as a dilevery driver for a long time.",
#                         "positive review"),
#                     Example(
#                         "uber eats is great for making income on the side. I have a side hustle now.",
#                         "positive review"),
#
#                     # negative tweets about frameworks
#                     Example(
#                         "Uber Eats made me loose mor money than I gained and I essentially paid them to work",
#                         "negative review"),
#                     Example(
#                         "I can barely brake even after paying for gas since I've been driving for uber eats.",
#                         "negative review"),
#
#                     # neutral tweets about frameworks
#                     Example("I delivered a sandwich from Subway. I work for uber eats",
#                             "neutral review"),
#                     Example("I brought a customer sushi from uber eats last night. They said they had no diarrhea", "neutral review"),
#                     Example("Driving for uber eats today and its nice outside.",
#                             "neutral review")
#                 ]
#             )
#
#             for classification in response.classifications:
#                 self.determine_results('react', classification)
#                 self.determine_results('next', classification)
#                 self.determine_results('vue', classification)
#                 self.determine_results('angular', classification)
#                 self.determine_results('node', classification)
#                 self.determine_results('ember', classification)
#
#         print("RESULTS:", self.results)
classifyObj = AnalysisBot()

classifyObj.classify_tweets()

data = ps.DataFrame(classifyObj.results)
data.to_csv('results.csv')


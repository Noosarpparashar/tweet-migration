import psycopg2
from psycopg2 import sql
import json



import snscrape.modules.twitter as sntwitter
import time
credFile = open('../tweet_migration/configs/secrets.json', "r")
data = json.loads(credFile.read())
connection = psycopg2.connect(user=data["user"],
                                  password=data["password"],
                                  host=data["host"],
                                  port=data["port"],
                                  database=data["database"])
cursor = connection.cursor()
query = "(bjp)"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    postgres_insert_query_twitter_tweet = """ INSERT INTO TWITTER.TWITTERTWEET (TWEET_ID, USER_ID, TWEET, RETWEET_COUNT) VALUES (%s,%s,%s,%s)"""
    record_to_insert_twitter_tweet = (str(vars(tweet)['id']), str(tweet.user.username), str(vars(tweet)['content']), str(vars(tweet)['retweetCount']))
    postgres_insert_query_twitter_user = """ INSERT INTO TWITTER.TWITTERUSER (USER_ID,USER_NAME) VALUES (%s,%s)"""
    record_to_insert_twitter_user = (str(tweet.user.id),str(tweet.user.username))
    cursor.execute(postgres_insert_query_twitter_tweet, record_to_insert_twitter_tweet)
    cursor.execute(postgres_insert_query_twitter_user, record_to_insert_twitter_user)
    connection.commit()
    print("Record inserted successfully into mobile table")

    time.sleep(1)
    print(1)

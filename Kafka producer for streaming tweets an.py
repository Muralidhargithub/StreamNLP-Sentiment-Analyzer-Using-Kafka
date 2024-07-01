# Kafka producer for streaming tweets and storing raw data in S3
from kafka import KafkaProducer
import tweepy
import json
import boto3

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Kafka server configuration
bootstrap_servers = ['localhost:9092']
topic_name = 'twitter_tweets'

# Connect to Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# S3 bucket configuration
raw_bucket_name = 'raws3bucket'
s3_client = boto3.client('s3')

# Twitter authentication and streaming setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Stream listener class
class KafkaStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = {
            'id_str': status.id_str,
            'text': status.text,
            'user': {
                'id': status.user.id,
                'screen_name': status.user.screen_name
            }
        }
        producer.send(topic_name, value=tweet)
        print(f'Tweet published to Kafka: {tweet["id_str"]}')

        # Store raw tweet in raws3bucket
        raw_key = f'raw_tweets/{tweet["id_str"]}.json'
        s3_client.put_object(Body=json.dumps(tweet), Bucket=raw_bucket_name, Key=raw_key)
        print(f'Raw tweet stored in {raw_bucket_name}: {tweet["id_str"]}')

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Disconnects the stream in case of rate limit error
        print(f'Error occurred: {status_code}')

# Start streaming
stream_listener = KafkaStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['keyword1', 'keyword2'])  # Replace with desired keywords(datascience, machinelearning, etc..)

import json
from textblob import TextBlob
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    raw_bucket_name = 'raws3bucket'
    result_bucket_name = 'results3bucket'

    for record in event['Records']:
        payload = record['value'].decode('utf-8')
        tweet = json.loads(payload)
        text = tweet['text']
        tweet_id = tweet['id_str']

        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'

        result = {
            'tweet_id': tweet_id,
            'text': text,
            'sentiment': sentiment,
            'polarity': polarity
        }

        # Store sentiment analysis result in results3bucket
        destination_key = f'sentiment/{tweet_id}.json'
        s3.Object(result_bucket_name, destination_key).put(Body=json.dumps(result))

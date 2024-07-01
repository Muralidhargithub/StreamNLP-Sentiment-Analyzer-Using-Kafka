# Twitter Sentiment Analysis with Kafka, AWS Lambda, Athena, and QuickSight

This project demonstrates how to stream Twitter data using Kafka, perform sentiment analysis on the tweets using AWS Lambda, store the results in Amazon S3, query the data with Amazon Athena, and visualize the sentiment analysis results using Amazon QuickSight.

## Project Files

- **kafka_producer.py**: Python script for streaming real-time tweets into a Kafka topic.
- **requirements.txt**: File listing all Python dependencies required for the project.
- **query.sql**: SQL queries for analyzing sentiment data stored in Amazon S3 using Amazon Athena.
- **gluecrawler.sh**: Shell script to create and manage an AWS Glue crawler for analyzing data in S3.
- **bucketcreation.sh**: Shell script to create the necessary S3 buckets (`raws3bucket` and `results3bucket`).
- **lambda_function.py**: AWS Lambda function for performing sentiment analysis triggered by Kafka messages.

## Prerequisites

Before running the project, make sure you have the following:

- AWS Account with necessary permissions to create and manage:
  - Kafka (if using MSK or another managed Kafka service)
  - Lambda functions
  - S3 buckets
  - Athena queries
  - QuickSight for visualization
- Twitter Developer Account with API credentials (consumer key, consumer secret, access token, access token secret)

## Setup

1. **Kafka Producer Setup**:
   - Install Kafka and set up a producer to stream tweets.
   - Replace `your_consumer_key`, `your_consumer_secret`, `your_access_token`, and `your_access_token_secret` with your Twitter API credentials.
   - Modify keywords in `stream.filter(track=['keyword1', 'keyword2'])` as per your search criteria.

2. **AWS Lambda Function**:
   - Create a Lambda function triggered by Kafka messages.
   - Implement sentiment analysis using TextBlob or another NLP library.
   - Store sentiment analysis results in the `results3bucket`.

3. **Amazon S3 Buckets**:
   - Run `bucketcreation.sh` to create `raws3bucket` and `results3bucket`.

4. **Amazon Athena Setup**:
   - Execute SQL queries from `query.sql` to create a database and table in Athena for sentiment analysis results.

5. **AWS Glue Crawler**:
   - Run `gluecrawler.sh` to create and manage an AWS Glue crawler for analyzing data in `results3bucket`.

6. **Amazon QuickSight Dashboard**:
   - Create a new analysis in QuickSight and connect it to Athena.
   - Build visualizations to analyze sentiment trends over time or by other dimensions.

## Commands and Configuration

### Kafka Producer

```bash


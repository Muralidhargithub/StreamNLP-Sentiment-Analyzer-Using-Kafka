aws glue create-crawler --name SentimentAnalysisCrawler \
    --role arn:aws:iam::123456789012:role/service-role/GlueCrawlerRole \
    --database SentimentAnalysisDB \
    --targets "S3Targets=[{Path='s3://results3bucket/sentiment/'}]"

aws glue start-crawler --name SentimentAnalysisCrawler
-- Count of Tweets by Sentiment
SELECT sentiment, COUNT(*) AS tweet_count
FROM sentiment_analysis_results
GROUP BY sentiment;

-- Average Polarity by Sentiment
SELECT sentiment, AVG(polarity) AS avg_polarity
FROM sentiment_analysis_results
GROUP BY sentiment;

-- Top 10 Positive Tweets
SELECT tweet_id, text, polarity
FROM sentiment_analysis_results
WHERE sentiment = 'positive'
ORDER BY polarity DESC
LIMIT 10;

-- Top 10 Negative Tweets
SELECT tweet_id, text, polarity
FROM sentiment_analysis_results
WHERE sentiment = 'negative'
ORDER BY polarity ASC
LIMIT 10;

-- Tweets with Neutral Sentiment
SELECT tweet_id, text, polarity
FROM sentiment_analysis_results
WHERE sentiment = 'neutral';

-- Trending Topics by Average Polarity
SELECT topic, AVG(polarity) AS avg_polarity
FROM (
    SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(text, ' ', 1), ' ', -1) AS topic, polarity
    FROM sentiment_analysis_results
) AS topics_polarity
GROUP BY topic
ORDER BY avg_polarity DESC
LIMIT 10;

-- Sentiment Distribution Over Time
SELECT date_trunc('day', CAST(created_at AS TIMESTAMP)) AS date,
       sentiment,
       COUNT(*) AS tweet_count
FROM sentiment_analysis_results
GROUP BY date_trunc('day', CAST(created_at AS TIMESTAMP)), sentiment
ORDER BY date ASC, sentiment ASC;

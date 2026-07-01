from textblob import TextBlob

class SentimentAgent:

    def analyze(self, text):

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            return "Positive", "Low"

        elif polarity < -0.2:
            return "Negative", "High"

        else:
            return "Neutral", "Medium"
import nltk
from nltk.corpus import gutenberg
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print("\nStarting download...\n")

nltk.download("gutenberg")
nltk.download("punkt_tab")
nltk.download("vader_lexicon")

print("\nDone!\n")



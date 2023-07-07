# Import the necessary libraries
from textblob import TextBlob  # For natural language processing and sentiment analysis
from newspaper import Article  # For web scraping and article extraction

# Define the URL of the article you want to analyze
url = 'https://cointelegraph.com/news/barnbridge-dao-calls-halt-on-work-amid-sec-investigation'

# Create an instance of the Article class with the given URL
article = Article(url)

# Download the article's HTML content
article.download()

# Parse the HTML and extract relevant information
article.parse()

# Apply natural language processing to the article's text
article.nlp()

# Extract the summarized text of the article
text = article.summary

# Print the summarized text
print(text)

# Create a TextBlob object to perform sentiment analysis on the summarized text
blob = TextBlob(text)

# Calculate the sentiment polarity of the summarized text (-1 to 1, where -1 is negative, 0 is neutral, and 1 is positive)
sentiment = blob.sentiment.polarity

# Print the sentiment polarity
print(sentiment)

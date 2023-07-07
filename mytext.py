# Import the necessary libraries
from textblob import TextBlob  # For natural language processing and sentiment analysis

# Open the file 'mytext.txt' in read mode
# The file should be in the same directory as the script
with open('mytext.txt', 'r') as f:
    # Read the contents of the file into a variable called 'text'
    text = f.read()

# Create a TextBlob object using the text from the file
blob = TextBlob(text)

# Calculate the sentiment polarity of the text (-1 to 1, where -1 is negative, 0 is neutral, and 1 is positive)
sentiment = blob.sentiment.polarity

# Print the sentiment polarity
print(sentiment)

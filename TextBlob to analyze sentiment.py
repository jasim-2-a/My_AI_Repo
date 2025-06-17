from textblob import TextBlob


user_input = input("Enter a text for sentiment analysis: ")

blob = TextBlob(user_input)


sentiment = blob.sentiment


print("\nSentiment Polarity: ", sentiment.polarity)
print("Sentiment Subjectivity: ", sentiment.subjectivity)


if sentiment.polarity > 0:
    print("The sentiment is Positive.")
elif sentiment.polarity < 0:
    print("The sentiment is Negative.")
else:
    print("The sentiment is Neutral.")

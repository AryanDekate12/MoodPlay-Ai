from textblob import TextBlob


def detect_mood(text):

    text = text.lower()

    # Keyword based detection (more accurate)
    if any(word in text for word in ["bored", "boring", "nothing to do"]):
        return "bored"

    if any(word in text for word in ["happy", "excited", "great", "good", "awesome"]):
        return "happy"

    if any(word in text for word in ["relaxed", "calm", "peaceful", "chill"]):
        return "relaxed"

    if any(word in text for word in ["angry", "mad", "frustrated", "rage"]):
        return "angry"

    if any(word in text for word in ["sad", "depressed", "upset", "down"]):
        return "sad"

    # Fallback to sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.4:
        return "happy"

    elif polarity > 0:
        return "relaxed"

    elif polarity == 0:
        return "bored"

    elif polarity > -0.4:
        return "sad"

    else:
        return "angry"
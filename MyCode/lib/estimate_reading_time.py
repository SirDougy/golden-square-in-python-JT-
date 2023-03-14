def estimate_reading_time(text):
    if not text:
        raise Exception('ERROR - no text entered')
    words = text.split()
    word_count = len(words)
    return word_count / 200



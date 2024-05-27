

def validate_input_data(text, sentiment):
    # Check if 'text' key is present
    if not text:
        return False, 'Missing / Empty parameter: text'

    # Check if 'sentiment' key is present
    if not sentiment:
        return False, 'Missing / Empty parameter: sentiment'

    # Check if 'sentiment' key is 'positive', 'negative' or 'neutral
    if sentiment not in ['positive', 'negative', 'neutral']:
        return False, 'Invalid sentiment value. Sentiment can be positive, negative or neutral'

    return True, None

import logging
from flask import request, jsonify
from app import app
from .request_utils import validate_input_data
from sentiment_text_extractor.extractor import SentimentTextExtractor

sentiment_text_extractor = SentimentTextExtractor()

# Configure logging
logging.basicConfig(filename='api.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


@app.route('/predict', methods=['GET'])
def predict():
    """Endpoint to predict text that express sentiment-related information from text.

    Returns:
        str: The selected text representing sentiment information extracted from the input text.
    """
    text = request.get_json().get('text')
    sentiment = request.get_json().get('sentiment')

    # Log request
    logging.info(f"Request received - Text: {text}, Sentiment: {sentiment}")

    # Validate input data
    is_valid, error_msg = validate_input_data(text, sentiment)
    if not is_valid:
        # Log validation error
        logging.error(f"Validation error: {error_msg}")
        return jsonify({'error': error_msg}), 400

    # Predict text
    selected_text = sentiment_text_extractor.extract(text, sentiment)

    # Log prediction
    logging.info(f"Prediction made - Selected Text: {selected_text}")

    return jsonify({'selected_text': selected_text})

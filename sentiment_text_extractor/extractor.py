from .tokenizer import Tokenizer
from .model import ModelWrapper


class SentimentTextExtractor:
    """Class for extracting words that express sentiment-related information from text."""

    def __init__(self):
        """Initialize the SentimentTextExtractor object."""
        self.tokenizer = Tokenizer()
        self.model_wrapper = ModelWrapper()

    def extract(self, text, sentiment):
        """Extract selected text that express sentiment-related information from input text.

        Args:
            text (str): The input text to extract sentiment from.
            sentiment (str): The sentiment associated with the text.

        Returns:
            str: The selected text representing sentiment information extracted from the input text.
        """
        input_ids, attention_mask, token_type_ids = self.tokenizer.preprocess_input(text, sentiment)
        start_logits, end_logits = self.model_wrapper.predict(input_ids, attention_mask, token_type_ids)
        selected_text = self.tokenizer.decode_output(start_logits, end_logits, text)
        return selected_text

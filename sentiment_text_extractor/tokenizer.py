import numpy as np
import tokenizers
from utils.extractor_params import VOCAB_PATH, MERGES_PATH, MAX_LEN
from utils.enums import SentimentId


class Tokenizer:
    """Class for tokenizing and preprocessing text data."""
    def __init__(self):
        """Initialize the Tokenizer object."""
        self.tokenizer = tokenizers.ByteLevelBPETokenizer(
            vocab=VOCAB_PATH,
            merges=MERGES_PATH,
            lowercase=True,
            add_prefix_space=True,
        )

    def preprocess_input(self, text, sentiment):
        """Preprocesses input text for model input.

        Args:
            text (str): The input text to be preprocessed.
            sentiment (str): The sentiment associated with the text.

        Returns:
            tuple: A tuple containing:
                - input_ids (numpy.ndarray): Processed input IDs.
                - attention_mask (numpy.ndarray): Attention mask for input.
                - token_type_ids (numpy.ndarray): Token type IDs for input.
        """
        input_ids = np.ones((1, MAX_LEN), dtype='int32')
        attention_mask = np.zeros((1, MAX_LEN), dtype='int32')
        token_type_ids = np.zeros((1, MAX_LEN), dtype='int32')

        text = " " + " ".join(text.split())
        encoded_text = self.tokenizer.encode(text)
        sentiment_token = SentimentId[sentiment.upper()].value
        input_ids[0, :len(encoded_text.ids) + 5] = [0] + encoded_text.ids + [2, 2] + [sentiment_token] + [2]
        attention_mask[0, :len(encoded_text.ids) + 5] = 1
        return input_ids, attention_mask, token_type_ids

    def decode_output(self, start_logits, end_logits, text):
        """Decodes model output into selected text.

        Args:
            start_logits (numpy.ndarray): Start logits predicted by the model.
            end_logits (numpy.ndarray): End logits predicted by the model.
            text (str): The original input text.

        Returns:
            str: The selected text extracted from the input text based on the logits.
        """
        selected_text = text
        start_idx = np.argmax(start_logits, axis=-1).item()
        end_idx = np.argmax(end_logits, axis=-1).item()

        if start_idx <= end_idx:
            text = " " + " ".join(text.split())
            encoded_text = self.tokenizer.encode(text)
            selected_text = self.tokenizer.decode(encoded_text.ids[start_idx-1:end_idx])
        return selected_text

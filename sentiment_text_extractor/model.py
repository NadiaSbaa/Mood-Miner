import tensorflow as tf
from transformers import RobertaConfig, TFRobertaModel
from utils.extractor_params import BEST_MODEL_PATH, BERT_PRETRAINED_MODEL, MAX_LEN, ROBERTA_CONFIG_PATH


class ModelWrapper:
    """Wrapper class for a TensorFlow model based on RoBERTa architecture."""

    def __init__(self):
        """Initialize the ModelWrapper object."""
        self.model = self.build_model()
        self.model.load_weights(BEST_MODEL_PATH)

    def build_model(self):
        """Build and compile the model."""
        ids = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
        att = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)
        tok = tf.keras.layers.Input((MAX_LEN,), dtype=tf.int32)

        config = RobertaConfig.from_pretrained(ROBERTA_CONFIG_PATH)
        bert_model = TFRobertaModel.from_pretrained(BERT_PRETRAINED_MODEL,
                                                    config=config)
        x = bert_model(ids, attention_mask=att, token_type_ids=tok)

        x1 = tf.keras.layers.Dropout(0.1)(x[0])
        x1 = tf.keras.layers.Conv1D(1, 1)(x1)
        x1 = tf.keras.layers.Flatten()(x1)
        x1 = tf.keras.layers.Activation('softmax')(x1)

        x2 = tf.keras.layers.Dropout(0.1)(x[0])
        x2 = tf.keras.layers.Conv1D(1, 1)(x2)
        x2 = tf.keras.layers.Flatten()(x2)
        x2 = tf.keras.layers.Activation('softmax')(x2)

        model = tf.keras.models.Model(inputs=[ids, att, tok], outputs=[x1, x2])
        optimizer = tf.keras.optimizers.Adam(learning_rate=3e-5)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer)

        return model

    def predict(self, input_ids, attention_mask, token_type_ids):
        """Predict start and end logits for input IDs, attention mask, and token type IDs.

        Args:
            input_ids (numpy.ndarray): Input IDs for tokenized text.
            attention_mask (numpy.ndarray): Attention mask for input IDs.
            token_type_ids (numpy.ndarray): Token type IDs for input IDs.

        Returns:
            tuple: A tuple containing:
                - start_logits (numpy.ndarray): Start logits predicted by the model.
                - end_logits (numpy.ndarray): End logits predicted by the model.
        """
        start_logits, end_logits = self.model.predict([input_ids, attention_mask, token_type_ids])
        return start_logits, end_logits

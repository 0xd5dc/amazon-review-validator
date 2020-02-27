import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SimpleRNN, GRU
from tensorflow.keras.preprocessing.text import Tokenizer
import logging

DATA_FILE = '../data/sample_us.tsv'
EMBEDDING_VECTOR_LENGTH = 32
TOP_WORDS = 50000
MAX_REVIEW_LENGTH = 600
NUM_WORDS = 50000


def split_pad(df):
    X_train, X_test, Y_train, Y_test = train_test_split(df['review_body'].values, \
                                                        df['label'].values, \
                                                        test_size=0.30, \
                                                        shuffle=True)
    logging.info("Y train mean: {0}, Y test mean: {1}".format(Y_train.mean(), Y_test.mean()))
    # tokenize the reviews text
    tokenizer = Tokenizer(num_words=NUM_WORDS)
    tokenizer.fit_on_texts(X_train)
    X_train_tok = tokenizer.texts_to_sequences(X_train)
    X_test_tok = tokenizer.texts_to_sequences(X_test)
    X_train_pad = sequence.pad_sequences(X_train_tok, maxlen=MAX_REVIEW_LENGTH)
    X_test_pad = sequence.pad_sequences(X_test_tok, maxlen=MAX_REVIEW_LENGTH)
    return X_train_pad, X_test_pad, Y_train, Y_test


if __name__ == '__main__':
    logging.basicConfig(filename='task.log', filemode='a', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # load processed data
    samples = pickle.load(open("verified_purchase_reviews.p", "rb"))
    # log sample mean ideally to be .5
    logging.info(samples['label'].mean())
    # split data
    X_train_pad, X_test_pad, Y_train, Y_test = split_pad(samples.sample(100))

    # compile models
    models = []
    models.append(Sequential())
    model = models[-1]
    model.add(Embedding(TOP_WORDS, EMBEDDING_VECTOR_LENGTH, input_length=MAX_REVIEW_LENGTH))
    # The output of SimpleRNN will be a 2D tensor of shape (batch_size, 128)
    model.add(SimpleRNN(128))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit and eval models
    for n in [1000, 10000, 50000]:
        X_train_pad, X_test_pad, Y_train, Y_test = split_pad(samples.sample(n))
        for model in models:
            model.fit(X_train_pad, Y_train, epochs=10, batch_size=64, validation_data=(X_test_pad, Y_test))
            # Final evaluation of the model on test data
            scores = model.evaluate(X_test_pad, Y_test, verbose=0)
            logging.info("loss: {0:2.2f}, accuracy {1:2.2f}".format(scores[0], scores[1]))

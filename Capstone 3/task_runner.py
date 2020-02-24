import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SimpleRNN, GRU
from tensorflow.keras.preprocessing.text import Tokenizer

DATA_FILE = '../data/sample_us.tsv'
EMBEDDING_VECTOR_LENGTH = 32
TOP_WORDS = 50000
MAX_REVIEW_LENGTH = 600
NUM_WORDS = 50000
if __name__ == '__main__':
    # load data
    df = pd.read_csv(DATA_FILE, sep='\t')
    # cast label to int
    df['label'] = (df['verified_purchase'] == 'Y').astype(int)
    reviews = df[['review_body', 'label']]
    # count the label to find imbalanced value
    counts = reviews.groupby("label")['label'].count().to_dict()
    sorted_counts = sorted(counts.items(), key=lambda kv: kv[1])
    # under-sampling
    samples = reviews[reviews['label'] == sorted_counts[1][0]].sample(sorted_counts[0][1])
    samples = pd.concat([samples, reviews[reviews['label'] == sorted_counts[0][0]]])
    print(samples.mean())
    # split data
    X_train, X_test, Y_train, Y_test = train_test_split(samples['review_body'].values, \
                                                        samples['label'].values, \
                                                        test_size=0.30, \
                                                        shuffle=True)
    print(Y_train.mean(), Y_test.mean())
    print(Y_train, Y_test)

    # tokenize the reviews text
    tokenizer = Tokenizer(num_words=NUM_WORDS)
    tokenizer.fit_on_texts(X_train)
    X_train_tok = tokenizer.texts_to_sequences(X_train)
    X_test_tok = tokenizer.texts_to_sequences(X_test)
    X_train_pad = sequence.pad_sequences(X_train_tok, maxlen=MAX_REVIEW_LENGTH)
    X_test_pad = sequence.pad_sequences(X_test_tok, maxlen=MAX_REVIEW_LENGTH)

    # compile models
    model = Sequential()
    model.add(Embedding(TOP_WORDS, EMBEDDING_VECTOR_LENGTH, input_length=MAX_REVIEW_LENGTH))
    # The output of SimpleRNN will be a 2D tensor of shape (batch_size, 128)
    model.add(SimpleRNN(128))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit and eval models
    # for model in models:
    print(model.summary())
    model.fit(X_train_pad, Y_train, epochs=10, batch_size=64, validation_data=(X_test_pad, Y_test))
    # Final evaluation of the model on test data
    scores = model.evaluate(X_test_pad, Y_test, verbose=0)
    print("Accuracy: %.2f%%" % (scores[1] * 100))

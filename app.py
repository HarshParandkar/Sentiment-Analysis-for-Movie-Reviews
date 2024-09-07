import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
model = load_model('imdb_sentiment_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

st.title('Sentiment Analysis Web App')

review = st.text_area("Enter your review:")
if st.button('Analyze'):
    sequences = tokenizer.texts_to_sequences([review])
    padded_sequences = pad_sequences(sequences, maxlen=200) 
    prediction = model.predict(padded_sequences)[0][0]
    sentiment = 'positive' if prediction > 0.6 else 'negative'
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction: {prediction}')

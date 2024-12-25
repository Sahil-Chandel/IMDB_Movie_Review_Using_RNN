# Step 1: Import Libraries
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Step 2: Load the IMDB Dataset and Word Index
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

try:
    # Load word index
    word_index = imdb.get_word_index()
    reverse_word_index = {value: key for key, value in word_index.items()}
    st.success("IMDB dataset word index loaded successfully.")
except Exception as e:
    st.error(f"Failed to load IMDB dataset word index: {e}")
    st.stop()

# Step 3: Load the Pre-trained Model
model_path = 'imdb_new.h5'

if os.path.exists(model_path):
    try:
        model = load_model(model_path)
        st.success("Pre-trained model loaded successfully.")
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()
else:
    st.error("Model file 'imdb.h5' not found. Please ensure the file exists in the correct directory.")
    st.stop()

# Step 4: Helper Functions
# Function to decode encoded reviews back to text
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Step 5: Streamlit User Interface
# Text area for user input
user_input = st.text_area('Movie Review', height=150)

# Classification button
if st.button('Classify'):
    if not user_input.strip():
        st.error("Please enter a valid movie review.")
    else:
        try:
            # Preprocess input
            preprocessed_input = preprocess_text(user_input)

            # Make prediction
            prediction = model.predict(preprocessed_input)
            sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

            # Display results
            st.subheader("Classification Result")
            st.write(f"Sentiment: **{sentiment}**")
            st.write(f"Prediction Score: **{prediction[0][0]:.4f}**")
        except Exception as e:
            st.error(f"Error during classification: {e}")
else:
    st.write("Enter a movie review and press 'Classify' to see the sentiment.")

# Step 6: Notes for Deployment
st.sidebar.title("Notes")
st.sidebar.info("""
- Ensure the `imdb.h5` model file is in the same directory as this script.
- The model expects input reviews of up to 500 words.
- Use a TensorFlow version compatible with the pre-trained model.
""")

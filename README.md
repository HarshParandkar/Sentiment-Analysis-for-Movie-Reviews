# **Sentiment Analysis Web App**

This project is a web application that performs sentiment analysis on movie reviews using a pre-trained machine learning model. The app is built using Streamlit and TensorFlow, and it allows users to input their own movie reviews to receive a sentiment prediction (positive or negative).

## **Table of Contents**

- Overview

- Installation

- Usage

- Model Training

- Project Structure

- Contributing

- License

**Overview**

This project uses a model trained on the IMDb movie reviews dataset to classify reviews as either positive or negative. The web interface is created using Streamlit, making it easy to test the model across different devices and platforms.

**Installation Prerequisites**

Python 3.8 or above

**Steps:**

Clone the repository.

Install the required packages from requirements.txt.

Run the Streamlit app using "streamlit run app.py".

**Usage**

1. After starting the app, you'll see a text area where you can enter a movie review.

2. Click the "Analyze" button to get the sentiment prediction.
   
3. The app will display whether the review is positive or negative along with the model's confidence score.

**Model Training**

The model was trained on the IMDb dataset using TensorFlow. The following steps were taken to prepare and train the model:

1. **Data Preprocessing:** Tokenization and padding of the text data.
2. **Model Architecture:** A simple neural network with an embedding layer, global average pooling, and dense layers.
3. **Training:** The model was trained for 10 epochs using binary crossentropy loss.


**Training Script**

The training script can be found in IMDB_Sentiment_Analysis.ipynb. It includes all the necessary steps to load the dataset, preprocess the data, train the model, and evaluate its performance.


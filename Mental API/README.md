# BI2-Project
Mental Health Diagnosis
# Suicide Prediction API

This repository contains the code for a suicide prediction API. The API uses a machine learning model to predict whether an individual is suicidal or not based on a text input.

## Getting the Dataset

The dataset used for this project was obtained from the Kaggle dataset "Suicide Risk Factors"  The dataset contains a variety of features about individuals, including the ID , text, and class.
## Preprocessing the Dataset

The dataset was preprocessed by removing missing values, converting categorical variables to numerical ones, and normalizing numerical variables. The text input was preprocessed by removing stop words, punctuation, and converting all text to lowercase.

## Training the Model

The machine learning model used for this project was a Naive Bayes classifier. The model was trained on a 70/30 split of the dataset, with 70% of the data used for training and 30% of the data used for testing.

## Testing the Model

The model was tested on the remaining 30% of the data. The accuracy of the model was 80%.

## Conclusion

The machine learning model used in this project is able to predict whether an individual is suicidal or not with an accuracy of 80%. This model could be used as a tool to help identify individuals who are at risk of suicide and provide them with the necessary support.

## Steps to run the API

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the API:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
4. To make a prediction, send a POST request to the `/predict` endpoint with the following JSON payload:
   ```json
   {
       "statement": "I am feeling very sad and hopeless."
   }
   ```
5. The API will return a JSON response with the following structure:
   ```json
   {
       "prediction": "suicidal"
   }
   ```

## Future Work

The accuracy of the model could be improved by using a larger dataset and more sophisticated machine learning techniques. The API could also be extended to include other features, such as the individual's mood and social support network.

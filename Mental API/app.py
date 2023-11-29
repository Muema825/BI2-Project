from fastapi import FastAPI
from bs4 import BeautifulSoup
import re
import pickle
import pandas as pd
import tensorflow as tf
import uvicorn
from MentalForm import MentalForm
import joblib
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import json



# Creating the app object
app = FastAPI()
# Load the pre-fitted vectorizer
loaded_vectorizer = joblib.load("C:/Users/muema/vectorizer.pickle", 'rb')

# Load the pre-trained model
VotingClassifiers = joblib.load('C:/Users/muema/NVBSuicideModel.pkl', 'rb')


@app.get("/")
def index():
     return {"message": "Welcome to the Suicide Prediction API"}

@app.get('/{name}')
def get_name(name: str):
     return {'Welcome to my Mental Health Medical Centre': f'{name}'}



@app.post('/predict', )
def predict_mentalform(data:MentalForm):
     data_dict = data.dict()
     print("Data Dictionary:", data_dict)
    
     statement = data_dict['statement']
     print("Statement:", statement)
     
     def preprocess(inp, vectorizer):
               inp = inp.lower() #convert to lower case 
               inp = inp.replace(r'[^\w\s]+', '') #remove punctuations
               inp = [word for word in inp.split() if word not in (stop_words)] #tokenize the sentence
               inp = ' '.join([ps.stem(i) for i in inp]) #stremming
               inputToModel = vectorizer.transform([inp]).toarray() #transform to vector form
               return inputToModel
     # Preprocess the data using the loaded vectorizer
     cleaned_statement = preprocess(statement, loaded_vectorizer)

     # Make predictions
     prediction = VotingClassifiers.predict(cleaned_statement)
     feedback = prediction.tolist()

     
     
     return(feedback)    
    
if __name__ == '__main__':
     uvicorn.run(app, host='127.0.0.1', port=8000)


    
     

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
from nltk.stem import PorterStemmer as ps
from nltk.corpus import stopwords
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
import joblib
import csv
import nltk

class modelPredict:
    isReady=False
    def __init__(self):
        self.dummy=0;

    def setup(self):
        self.model=joblib.load('app/model/model.pkl')
        self.feats=list(csv.reader(open('app/model/sparse_feat.csv')))
        self.isReady=True
    
    def isModelReady(self):
        return self.isReady
    
    def predictSentiment(self,input_string):
        print("Predict: "+input_string);
        stm=ps() # Protor Stemmer
        stp=stopwords.words('english')
        ## remove links and format
        input_string=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', input_string)
        input_string=re.sub('[^a-zA-Z]',' ',input_string).lower()
        ## string stemming
        tmps = ""
        for i in input_string.split():
            if stm.stem(i) not in stp:
                tmps += (stm.stem(i) + ' ');
            test_string = tmps
        sparseMat=[]
        for i in self.feats[0]:
            if i in test_string.split():
               sparseMat.append(1)
            else:
                sparseMat.append(0)
        return self.model.predict([sparseMat])
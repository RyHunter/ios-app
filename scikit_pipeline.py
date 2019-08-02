import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import config
import database.db as db

dbSelect = db.connect(config.DATABASE['user'], config.DATABASE['password'])

data = pd.read_sql_query("""SELECT  p.id, 
		p.impressions_ratio,       
		wc.noun_fraction, 
		wc.pronoun_fraction, 
		wc.verb_fraction, 
		wc.adjective_fraction, 
		wc.adverb_fraction, 
		wc.total_words,
        s.afinn_sentiment,
        s.polarity    
        FROM posts p
        JOIN word_count wc ON p.id=wc.post_id
        JOIN sentiment s ON p.id=s.post_id;
        """, dbSelect, "id")

y = data.impressions_ratio
X = data.drop('impressions_ratio', axis=1)

print ("Splitting test set...")
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=123)

print ("Preprocessing...")
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print ("Tuning hyperparameters...")
pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))

hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}

print ("Training model...")
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)

print ("Running test set...")
y_pred = clf.predict(X_test)
rSquared = r2_score(y_test, y_pred)
meanSquaredError = mean_squared_error(y_test, y_pred)

print (rSquared, meanSquaredError)
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

X_train = pd.read_sql_query("""
        SELECT  
        p.id, 
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
        JOIN sentiment s ON p.id=s.post_id
        WHERE p.created_time < "2019-01-01"
        ORDER BY p.created_time DESC;
        """, dbSelect, "id")

X_test = pd.read_sql_query("""
        SELECT  
        p.id, 
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
        JOIN sentiment s ON p.id=s.post_id
        WHERE p.created_time >= "2019-01-01"
        ORDER BY p.created_time DESC;
        """, dbSelect, "id")

y_train =pd.read_sql_query("""
        SELECT     
        p.id, 
		p.impressions_ratio     
        FROM posts p
        WHERE p.created_time < "2019-01-01"
        ORDER BY p.created_time DESC;
        """, dbSelect, "id")

y_train = y_train.impressions_ratio

y_test =pd.read_sql_query("""
        SELECT  
        p.id, 
		p.impressions_ratio     
        FROM posts p
        WHERE p.created_time >= "2019-01-01"
        ORDER BY p.created_time DESC;
        """, dbSelect, "id")

y_test = y_test.impressions_ratio

print ("Preprocessing...")
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print ("Tuning hyperparameters...")
pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))

hyperparameters = {'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}

print ("Training model...")
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
clf.fit(X_train, y_train)

print ("Running test set...")
y_pred = clf.predict(X_test)
rSquared = r2_score(y_test, y_pred)
meanSquaredError = mean_squared_error(y_test, y_pred)

print ("Writing known values to csv...")
y_test.to_csv("test_results.csv", header=True)
results_file = open("test_results.csv", 'a')

print ("Writing predicted values to csv...")
results_file.write("predicted_impressions_ratio\n")
for element in np.nditer(y_pred):
    results_file.write(str(element))
    results_file.write("\n")

results_file.close()

print ("R squared: {} Mean Squared Error: {}".format(rSquared, meanSquaredError))
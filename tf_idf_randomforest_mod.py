#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:24:11 2021

@author: isaachorwitz
"""

import pandas as pd
import pickle
from nltk.corpus import stopwords

def my_tf_idf(var, path_in):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    import pickle
    my_tf_idf = TfidfVectorizer()
    my_tf_idf_vec = pd.DataFrame(my_tf_idf.fit_transform(var).toarray())
    my_tf_idf_vec.columns = my_tf_idf.get_feature_names()
    pickle.dump(my_tf_idf, open(path_in + "tf_idf.pkl", "wb"),protocol=4)
    pickle.dump(my_tf_idf_vec, open(path_in + "tf_idf_df.pkl", "wb" ),protocol=4 )
    return my_tf_idf_vec

df = pd.read_excel("/Users/isaachorwitz/Downloads/Depression & Anxiety Facebook page Comments Text.xlsx")
df.columns = ['text']
df['label'] = 1
randtweets = pd.DataFrame(pd.read_csv("/Users/isaachorwitz/random_tweets.csv").text)
randtweets['label'] = 0
df = pd.concat([df,randtweets])
from sklearn.utils import shuffle
df = shuffle(df)
df = df.sample(n=1000, random_state=1)

def rem_sw(var):
    from nltk.corpus import stopwords
    sw = stopwords.words('english')
    tmp = var.split() #tokenize
    fin_var = [word for word in tmp if word not in sw]
    fin_var = ' '.join(fin_var)
    return fin_var

df.text = df.text.apply(rem_sw)

tf_idfs = my_tf_idf(df.text,"/Users/isaachorwitz/Downloads/")


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(
    tf_idfs, df['label'], test_size=0.20, random_state=42)

rf = RandomForestClassifier(random_state=123)
parameters = {'max_depth':[10, 100], 'n_estimators':[10, 100]}

clf = GridSearchCV(rf, parameters, cv=5)
clf.fit(X_train, y_train)
grid_y_pred = clf.best_estimator_.predict(X_test)

the_metrics = precision_recall_fscore_support(
    y_test, grid_y_pred, average='weighted')
print (the_metrics)    

print (clf.best_score_)
print (clf.best_params_)

rf_opt = RandomForestClassifier(**clf.best_params_, random_state=123)
rf_opt.fit(X_train, y_train)

### HERE IS WHERE I PICKLE DUMP THE MODEL ###

pickle.dump(rf_opt, open("/Users/isaachorwitz/Downloads/" + "model.pkl", "wb" ) )

### 

y_pred = rf_opt.predict(X_test)
print (confusion_matrix(y_test, y_pred))

rf_opt.feature_importances_

# predictions

tweet_df = pd.read_csv("/Users/isaachorwitz/df.csv")

tf_idfs = pickle.load(open("/Users/isaachorwitz/Downloads/tf_idf.pkl", "rb"))
tf_idf = tf_idfs.transform(tweet_df.text).toarray()
model = pickle.load(open("/Users/isaachorwitz/Downloads/model.pkl","rb"))
the_pred = model.predict(tf_idf)
preds = pd.Series(the_pred).T
preds.to_csv("depressed_preds.csv")
probs = pd.DataFrame(model.predict_proba(tf_idf))
the_scores = pd.concat([preds, probs], axis=1)
the_scores.columns = ["class_label", "likelihood_0","likelihood_1"]

# viz
import matplotlib.pyplot as plt
from sklearn import tree
fn=tf_idfs.columns
cn=df['label'].to_list()
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(rf_opt.estimators_[0],
               feature_names = tf_idfs.columns, 
               class_names=df['label'].astype(str).to_list());
fig.savefig('rf_individualtree.png')

# feature importance
featureImp = []
for feat, importance in zip(tf_idfs.columns, rf_opt.feature_importances_):  
    temp = [feat, importance*100]
    featureImp.append(temp)

fT_df = pd.DataFrame(featureImp, columns = ['Feature', 'Importance'])
fT_df = fT_df.sort_values('Importance', ascending = False)

interest = ['anxiety', 'depression','bipolar','horrible','time','meds','struggle','feel','help','disorder','feeling','think','panic','severe']

# visualize tf_idf mat

import pandas as pd
y_test = pd.Series(y_test)
y_pred = pd.Series(y_pred)

pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)




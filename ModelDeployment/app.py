#import libraries
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)
ada_model = pickle.load(open('./models/ada_trained_model.pkl', 'rb'))
bag_model = pickle.load(open('./models/bag_trained_model.pkl', 'rb'))
dec_model = pickle.load(open('./models/dec_trained_model.pkl', 'rb'))
extra_model = pickle.load(open('./models/extra_trained_model.pkl', 'rb'))
gbc_model = pickle.load(open('./models/gbc_trained_model.pkl', 'rb'))
lr_model = pickle.load(open('./models/lr_trained_model.pkl', 'rb'))
lsvm_model = pickle.load(open('./models/lsvm_trained_model.pkl', 'rb'))
mnb_model = pickle.load(open('./models/mnb_trained_model.pkl', 'rb'))
rfc_model = pickle.load(open('./models/rfc_trained_model.pkl', 'rb'))
sgd_model = pickle.load(open('./models/sgd_trained_model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open("./models/vectorizer.pickle", 'rb')) 
dic = {0: "Negative", 1: "Positive"}

#Route to handle HOME
@app.route('/')
def index():
    return render_template('index.html')

#Route to handle PREDICTED RESULT
@app.route('/', methods = ['POST'])
def recognize():
    
    rev = request.form['review']
    rev = [rev]
    rev = loaded_vectorizer.transform(rev)

    pre_ada = ada_model.predict(rev)
    pre_bag = bag_model.predict(rev)
    pre_dec = dec_model.predict(rev)
    pre_extra = extra_model.predict(rev)
    pre_gbc = gbc_model.predict(rev)
    pre_lr = lr_model.predict(rev)
    pre_lsvm = lsvm_model.predict(rev)
    pre_mnb = mnb_model.predict(rev)
    pre_rfc = rfc_model.predict(rev)
    pre_sgd = sgd_model.predict(rev)

    pre_ada = dic[int(pre_ada)]
    pre_bag = dic[int(pre_bag)]
    pre_dec = dic[int(pre_dec)]
    pre_extra = dic[int(pre_extra)]
    pre_gbc = dic[int(pre_gbc)]
    pre_lr = dic[int(pre_lr)]
    pre_lsvm = dic[int(pre_lsvm)]
    pre_mnb = dic[int(pre_mnb)]
    pre_rfc = dic[int(pre_rfc)]
    pre_sgd = dic[int(pre_sgd)]


    prediction = [["Ada Model",pre_ada],["Logistic Regression",pre_lr],["Multinomial Naive Bayes",pre_mnb],["Decision Tree Classifier",pre_dec],["Gradient Boosting Classifier",pre_gbc],
    ["Extra Tree Classifier",pre_extra],["Bagging meta-estimator",pre_bag],["Stochastic Gradient Descent",pre_sgd],["Random Forest Classifier",pre_rfc],["Linear Support Vector Machines",pre_lsvm]]
    print(prediction)
    return render_template('index.html',show = 'show',prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)



    



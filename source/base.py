from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import os
from keras.models import load_model

from data_preprocessing import Preprocessing
from predict import Predict
from get_data import Get_data
from sentiment_analysis import Sentiment_analysis


app = Flask(__name__)
CORS(app)

def getmodel():
    global model
    model_file_name = 'model_crr.h5'
    model_file_path = 'E:/ML/proj/fake_real_news_ext/model/' + model_file_name

    if (os.path.isfile(model_file_path)):
        model = load_model(model_file_path)
        print('**Model loaded!!**')

    return model

print('loading model...')
model = getmodel()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    url = message['name']
    print(url)

    get_data = Get_data()
    soup = get_data.getsoup(url)

    #sentiment analysis
    sentiment_analysis = Sentiment_analysis(soup)
    polariy_score = sentiment_analysis.polarity_interpretation()
    subjectivity_score = sentiment_analysis.subjectivity_interpretation()

    preprocessing = Preprocessing(soup)
    X_final = preprocessing.getCleanNews()

    predict = Predict(X_final, model)
    prediction = predict.model_prediction()
    print(prediction)

    response = {
        'prediction': {
            'news': str(prediction) + '%',
            'polatiry': polariy_score,
            'subjectivity': subjectivity_score
        }
    }

    return jsonify(response)

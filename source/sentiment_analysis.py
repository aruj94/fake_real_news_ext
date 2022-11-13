from get_data import Get_data
from data_preprocessing import Preprocessing
from textblob import TextBlob

class Sentiment_analysis():
    def __init__(self, soup):
        self.soup = soup
        self.get_data = Get_data()

    def analysis(self):
        sentiments = {}

        preprocessing = Preprocessing(self.soup)
        news_dict = preprocessing.createDict()
        text = news_dict['complete_news']
        sentA = TextBlob(text)
        sentiments['Polarity'] = sentA.sentiment.polarity
        sentiments['Subjectivity'] = sentA.sentiment.subjectivity

        return sentiments

    def polarity_interpretation(self):
        sentiments = self.analysis()

        if sentiments['Polarity'] >= 0.05:
            score = 'positive'

        elif -.05 < sentiments['Polarity'] < 0.05:
            score = 'neutral'

        else:
            score = 'negative'

        return score

    def subjectivity_interpretation(self):
        sentiments = self.analysis()

        if sentiments['Subjectivity'] >= 0.75:
            score = 'opinionated'

        elif 0.50 <= sentiments['Subjectivity'] < 0.75:
            score = 'somewhat opinionated'

        elif 0.25 <= sentiments['Subjectivity'] < 0.50:
            score = 'somewhat objective'

        else:
            score = 'objective and factual'

        return score
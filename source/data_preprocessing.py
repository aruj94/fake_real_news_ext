import re
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.preprocessing.text import one_hot
from keras.utils import pad_sequences
from get_data import Get_data


class Preprocessing():
    def __init__(self, soup):
        self.soup = soup
        self.get_data = Get_data()

    def createDict(self):
        news_dict = {}

        #soup = self.get_data.getsoup(url)
        headline = self.get_data.getheadline(self.soup)
        date = self.get_data.getdate(self.soup)
        subject = self.get_data.getsubject(self.soup)
        text = self.get_data.getcontent(self.soup)

        news_dict['complete_news'] = headline + text
        news_dict['date'] = date
        news_dict['subject'] = subject[1:]

        return news_dict

    def reviewCleaning(self, text):
        '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
                and remove words containing numbers.'''
        text = str(text).lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)

        return text

    def punctuationCleaning(self, cleannews_dict):
        cleannews_dict['complete_news'] = self.reviewCleaning(cleannews_dict['complete_news'])

        # Stop words cleaning
        stop = stopwords.words('english')
        x = cleannews_dict['complete_news']
        cleannews_dict['complete_news'] = ' '.join([word for word in x.split() if word not in stop])

        return cleannews_dict

    def removeStopWords(self, completenews):
        stop_words = set(stopwords.words("english"))
        ps = PorterStemmer()

        news = re.sub('[^a-zA-Z]', ' ', completenews)
        news = news.lower()
        news = news.split()
        news = [ps.stem(word) for word in news if not word in stop_words]
        news = ' '.join(news)

        return news

    def encoding(self, news):
        # using a vocabulary size 25% larger than the word size to increase the uniqueness of the hashes
        onehot_repr = one_hot(news, n=10000)
        X_final = pad_sequences([onehot_repr], padding='pre', maxlen=5000)

        return X_final

    def getCleanNews(self):
        cleannews_dict = self.createDict()
        cleannews_dict = self.punctuationCleaning(cleannews_dict)
        cleannews_dict['complete_news'] = self.removeStopWords(cleannews_dict['complete_news'])
        X_final = self.encoding(cleannews_dict['complete_news'])

        return X_final
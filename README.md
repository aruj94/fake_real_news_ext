"# fake_real_news_ext" 

Code for a Mozilla extension to classify news articles.
To run the extension, add the manifest file to firefox temp addons. You will also need to run a local flask server for the model to process text.
Make sure to set -> FLASK_APP=base.py
then you can -> flask run

Please check if the website you're using this extension on permits web scrapping or not because this ext uses web scrapping.
For testing purposes, you can use kaggle news datasets, create your own html page for any news article from that dataset and start your own server using python. You can use the command -> python -m http.server 8000 to setup the python server. '8000' here is the port number.

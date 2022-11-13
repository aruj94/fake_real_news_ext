from bs4 import BeautifulSoup
import requests
import re


class Get_data():

    '''
    def get_url(self):
        #informationtransmission.sendMessage(informationtransmission.encodeMessage("getting url..."))
        informationtransmission = Informationtransmission()
        url = informationtransmission.getMessage()
        #informationtransmission.sendMessage(informationtransmission.encodeMessage("soup url"))
        #url = 'http://localhost:8000'
        return url
    '''

    def getsoup(self, url):
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')

        return soup

    def getheadline(self, soup):
        headerlist = soup.find_all(re.compile('^h[1-6]'))
        for header in headerlist:
            return header.text

    def getdate(self, soup):
        date = soup.find("span", {"class": "date"})
        for date in date:
            return date

    def getsubject(self, soup):
        tags = soup.find("p", {"class": "tags"})
        for tag in tags:
            return tag

    def getcontent(self, soup):
        content = soup.find("p", {"class": "content"})
        for content in content:
            return content

"""
VaderSentiment.py

Deze file bevat functies om je te helpen gebruik te maken van de VaderSentiment-library.
Hiermee kun je stukken tekst analyseren, om in te schatten of de tekst positief, neutraal of
negatief is.

Bron VaderSentiment: https://github.com/cjhutto/vaderSentiment

@author:    Lina Blijleven <lina.blijleven@hu.nl>
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class VaderSentiment:
    """
    Class implementation
    """

    def __init__(self):
        """
        Constructor
        """
        self._analyzer = SentimentIntensityAnalyzer()

    def analyse_sentiments(self, sentences: list):
        """

        :param      sentences:  Meerdere (ongerelateerde) teksten om te
                                analyseren.
        :return:    dict:       Positive, neutral, negative en compound scores
        """
        return [self._analyzer.polarity_scores(s) for s in sentences]

    def analyse_sentiment(self, sentence: str):
        """
        Analyseer een enkele tekst om het sentiment te bepalen.

        :param:     sentence:   Tekst om te analyseren
        :return:    list:       Lijst met dictionaries voor de scores per tekst
        """
        return self._analyzer.polarity_scores(sentence)




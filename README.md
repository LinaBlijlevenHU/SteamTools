# SteamTools

Deze repository bevat een aantal voorbeelden en helper-modules voor project Steam. Elke tool wordt even apart behandeld in deze README, zodat je zelf de onderdelen uit kunt kiezen die je wil gebruiken.

## SteamSpy

Dit is de API/website waar de data in het steam.json-bestand vandaan komt. Je kunt deze zelf ook benaderen voor real-time data.

Let op: deze API is niet van Steam zelf. Deze scrapet data van de website van Steam, wat fout kan gaan als Steam de structuur van de website aanpast. Zorg dus dat je applicatie niet afhankelijk is van deze data.

## VaderSentiment

Dit is een AI [library](https://github.com/cjhutto/vaderSentiment) die helpt met het inschatten van het sentiment van teksten.

Installeer eerst de library met het volgende commando, of gebruik het tabje 'Packages' in PyCharm:
`pip install vader-sentiment`

`SentimentAnalyser.py` bevat een aantal hulpfuncties. Dit bestand heb je dan ook nodig in je eigen code, of je kunt de 
Vader-library direct implementeren als je dit prettiger vindt. Importeer de code met de volgende regel:

`from SentimentAnalyser import SentimentAnalyser`

Dit kun je doen door de code te plaatsen in dezelfde folder. Als de code in een andere folder wordt geplaatst, zul je zelf 
moeten zorgen dat de module correct geïmporteerd wordt.



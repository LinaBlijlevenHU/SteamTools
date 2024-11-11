# SteamTools

Deze repository bevat een aantal voorbeelden en helper-modules voor project Steam. Elke tool wordt even apart behandeld in deze README, zodat je zelf de onderdelen uit kunt kiezen die je wil gebruiken.

## GUI's

Voor Steam kun je meerdere technieken gebruiken om een grafische user interface (GUI) 
op te bouwen.

1. TKinter: dit is een library die standaard bij Python geleverd wordt. 
Hiermee maak je makkelijk interfaces die op veel verschillende apparaten kunnen draaien.
2. Flask web app: Flask is een Python-library die speciaal gemaakt is om webapplicaties op te 
zetten. Deze is gebruiksvriendelijk om te leren en populair binnen Python.
3. Bootstrap: met Bootstrap kun je makkelijk een grafische gebruikersinterface bouwen d.m.v.
HTML/CSS en JavaScript.

Binnen Project Steam mag je zelf kiezen welke technologie je gebruikt. Ook andere technologieën zijn 
mogelijk in overleg met je docenten.

Zie ook het [startersproject voor Flask](https://github.com/LinaBlijlevenHU/flask-base-project).

## Data naar de PI sturen

De Raspberry PI Pico W heeft ook wi-fi, maar dit geldt niet voor 
elke versie van de RPI. Om data van een API naar je RPI Pico 
zonder wi-fi te krijgen, moet je via seriële verbinding data 
naar je Pi sturen. Pepijn heeft hier een scriptje 
`serial_data_sending.py` voor geschreven, dat je ter inspiratie kan gebruiken.

## SteamSpy

Dit is de API/website waar de data in het steam.json-bestand 
vandaan komt. Je kunt deze zelf ook benaderen voor real-time data, hoewel 
de Steam API zelf beter onderhouden wordt.

Om deze API te gebruiken heb je alleen de requests-library nodig.

Let op: deze API is niet van Steam zelf. Deze scrapet data van de website van Steam, wat fout kan gaan als Steam de structuur van de website aanpast. 
Zorg dus dat je applicatie niet afhankelijk is van deze data. Daarnaast kan de API alleen publieke profielen bekijken, waardoor 
de data niet 100% representatief is voor alle Steam-gebruikers.

```json
{
  'appid': 10, 
  'name': 'Counter-Strike', 
  'developer': 'Valve', 
  'publisher': 'Valve', 
  'score_rank': '', 
  'positive': 225272, 
  'negative': 5860, 
  'userscore': 0, 
  'owners': '10,000,000 .. 20,000,000', 
  'average_forever': 11458, 
  'average_2weeks': 131, 
  'median_forever': 226, 
  'median_2weeks': 79, 
  'price': '999', 
  'initialprice': '999', 
  'discount': '0', 
  'ccu': 11917, 
  'languages': 'English, French, German, Italian, Spanish - Spain, Simplified Chinese, Traditional Chinese, Korean', 'genre': 'Action',
  'tags': {'Action': 5454, 'FPS': 4880, 'Multiplayer': 3431, 'Shooter': 3381, 'Classic': 2812, 'Team-Based': 1886, 'First-Person': 1724, 'Competitive': 1623, 'Tactical': 1361, "1990's": 1220, 'e-sports': 1208, 'PvP': 898, 'Old School': 793, 'Military': 641, 'Strategy': 624, 'Survival': 306, 'Score Attack': 292, '1980s': 272, 'Assassin': 231, 'Nostalgia': 167}
}
```

## VaderSentiment

Dit is een AI [library](https://github.com/cjhutto/vaderSentiment) die helpt met het inschatten van het sentiment van teksten.

Installeer eerst de library met het volgende commando, of gebruik het tabje 'Packages' in PyCharm:

`pip install vader-sentiment`

`SentimentAnalyser.py` bevat een aantal hulpfuncties. Dit bestand heb je dan ook nodig in je eigen code, of je kunt de 
Vader-library direct implementeren als je dit prettiger vindt. Importeer de code met de volgende regel:

`from SentimentAnalyser import SentimentAnalyser`

Dit kun je doen door de code te plaatsen in dezelfde folder. Als de code in een andere folder wordt geplaatst, zul je zelf 
moeten zorgen dat de module correct geïmporteerd wordt. Hiermee zou je bijvoorbeeld kunnen beoordelen 
of een geplaatste opmerking positief of negatief is.

### Voorbeeld output

```json
{
  'neg': 0.0,             // Negatief sentiment
  'neu': 0.513,           // Neutraal sentiment
  'pos': 0.487,           // Positief sentiment
  'compound': 0.431       // Compounded score
}
```


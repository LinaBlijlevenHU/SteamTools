"""
vader_example.py

Welkom bij het voorbeeldscript voor VaderSentiment. We behandelen
hier twee manieren om teksten te analyseren:

1. Stuk voor stuk met de functie analyse_sentiment
2. Met meerdere tegelijkertijd (in een lijst) met de functie analyse_sentiments. Het resultaat
hiervoor krijg je dan ook weer terug in een lijst met dezelfde volgorde.

De output die je per zin terug krijgt ziet er bijvoorbeeld zo uit:
{'neg': 0.326, 'neu': 0.674, 'pos': 0.0, 'compound': -0.4404}

Deze output bestaat uit 4 scores:
- neg:      Negativiteit
- neu:      Neutraliteit
- pos:      Positiviteit
- compound: Gecombineerde score

Over het algemeen wordt alleen de compound-score gebruikt. Deze
geeft een algemeen inzicht in het sentiment van het bericht.

Positieve tekst: compound score >= 0.05
Neutrale tekst: (compound score > -0.05) and (compound score < 0.05)
Negatieve tekst: compound score <= -0.05

@author Lina Blijleven      <lina.blijleven@hu.nl>
"""
# Met deze regel importeer je mijn helperklasse
from SentimentAnalyser import SentimentAnalyser

# Enkel zinnetje om te analyseren
txt = "Ik ben een zeer verdrietig zinnetje :("

# Voorbeelden van zinnetjes om te analyseren:
# Je kunt prima allerlei leestekens, hoofdletters, emojis etc. gebruiken in de
# teksten die je analyseert.
sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]

# Bouw de analyser; dit moeten we even doen ter voorbereiding!
analyser = SentimentAnalyser()

# Analyseer één tekst (analyse_sentiment)
result = analyser.analyse_sentiment(txt)
print(f"{txt}: {result}")
print(f"{txt} compound score: {result['compound']}")

# Analyseer meerdere teksten (analyse_sentimentS (meervoud))
# Let op: deze worden behandeld alsof ze niet gerelateerd aan elkaar zijn. Dat betekent dat de
# verschillende teksten in de lijst elkaars score niet beïnvloeden.
results = analyser.analyse_sentiments(sentences)

# Print de originele teksten en scores
for i in range(len(results)):
    print(f"{sentences[i]}: {results[i]}")
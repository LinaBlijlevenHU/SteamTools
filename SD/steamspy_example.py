"""
steamspy_example.py

Voorbeeld voor het gebruiken van de SteamSpy API.
Dit bestandje is alleen bedoeld als een voorbeeld.

@author     Lina Blijleven  <lina.blijleven@hu.nl>
"""

# Met deze import importeer je mijn hulperfunctie
from steam_spy import get_app_details

# App ID van de app die via Steam wordt verkocht.
appid = 10

# Roep de hulpfunctie aan
app_details = get_app_details(appid)

# Als het goed gaat krijgen we een dictionary met details.
if app_details:
    print(f"App ID {appid} details:")
    print(app_details)
# Anders hebben we None
else:
    print("Failed to retrieve app details.")

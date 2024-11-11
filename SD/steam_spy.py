"""
steam_spy.py

Dit bestand bevat een hulpfunctie om de SteamSpy-API aan te roepen. Om deze te gebruiken moet je
de functie importeren, je mag dit bestand dus overnemen in je eigen project met de correcte bronvermelding.

Je hebt voor het opvragen van gamedata alleen de ID van een game nodig, zoals deze voorkomt in het JSON-bestand.
Zie de README voor voorbeeld-output.

@author Lina Blijleven  <lina.blijleven@hu.nl>
"""
# Standaard-library voor verzoeken
import requests


def get_app_details(appid):
    """
    Vraag wat data op over een spel met de SteamSpy-API.

    :param  appid:      ID van de Steam-game (zelfde als in de JSON)
    :return dict|None:  Data over de game of None
    """
    api_url = f'https://steamspy.com/api.php?request=appdetails&appid={appid}'

    try:
        # Verstuur het verzoek en laat eventuele HTTP-errors zien
        response = requests.get(api_url)
        response.raise_for_status()

        # Zet de response om naar JSON
        data = response.json()

        # Return the data
        return data

    # Vang exceptions af, zodat we netjes de error uit kunnen printen.
    # De functie retourneert vervolgens None, dus check altijd of je correcte output krijgt!
    except requests.exceptions.RequestException as e:
        # We printen het error-bericht uit, zodat we kunnen zien
        # wat voor probleem we precies hebben.
        print(f"Error: {e}")
        return None

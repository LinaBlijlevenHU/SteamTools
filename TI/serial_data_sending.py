"""
serial_data_sending.py

In dit bestand laat ik zien hoe je data van je laptop via de Serial verbinding (USB) data kan sturen naar je pico

Dit kan heel handig zijn als je bijvoorbeeld data vanuit een API op een LCD schermpje wilt zetten op de pico
Onze Raspberry pi pico heeft namelijk geen wifi antenne en kan dus zelf geen API requests hebben.
Maar het is wel heel leuk om data via je pico te laten zien

@author     Pepijn Devue  <pepijn.devue@hu.nl>
"""


"""
Allereerst de code voor je laptop
---------------------------------------------------------------------------------------------------------------------------------------
Op je laptop wil je sowieso de library serial hebben geinstalleerd met pip

Verbind je pico met je laptop en kijk via je device manager op welke COM-poort hij verbonden is

Vul de naam van deze COM-poort in in de code hieronder, deze code speel je af op je laptop
"""

import serial

# Verbind met de serial port met een baudrate van 9600
serial_port = serial.Serial('COMx', 9600)  # TODO: vul hier de goede COM poort in in plaats van 'COMx'

# Hier wat voorbeeld code om strings door te sturen
try:
    while True:
        # Vraag de gebruiker een input te geven
        data_to_send = input("Enter data to send: ")

        # Encode deze string en stuur het door de serial poort
        serial_port.write(data_to_send.encode())

# Sluit netjes af als je verbinding verliest
except KeyboardInterrupt:
    print("Exiting program")
    serial_port.close()


"""
Hieronder de code voor je Raspberry pi pico
-------------------------------------------------------------------------------------------------------------------------------------------
Zorg ervoor dat je op je pico de library machine hebt geïnstalleerd
"""

import machine

# Verbind met de serial port met een baudrate 9600, pas tx en rx aan gebaseerd op je pico setup
serial_port = machine.UART(0, baudrate=9600, tx=0, rx=1)

while True:
    # Check of er nieuwe informatie is gekregen
    if serial_port.any():
        # Lees de volgende line van de serial port, decode deze en strip deze
        received_data = serial_port.readline().decode().strip()

        # TODO: schrijf hier de code die iets doet met deze data
        #       Dit kan zijn: display op LCD, gebruik om verschillende lampjes te laten branden, etc
        print(f"Received data: {received_data}")

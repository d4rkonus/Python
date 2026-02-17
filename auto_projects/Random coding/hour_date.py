#!/usr/bin/python3

from datetime import datetime
from zoneinfo import ZoneInfo

# Mensaje para el usuario
print("\nDime el nombre de un país y te diré la hora y fecha exacta en su capital.\n")

hora_ahora = input("[+] Nombre del país: ").strip().lower()

# Diccionario de países y sus zonas horarias
zonas_horarias = {

    # 🇪🇺 Europa
    "españa": "Europe/Madrid",
    "irlanda": "Europe/Dublin",
    "alemania": "Europe/Berlin",
    "francia": "Europe/Paris",
    "italia": "Europe/Rome",
    "portugal": "Europe/Lisbon",
    "reino unido": "Europe/London",
    "países bajos": "Europe/Amsterdam",
    "suiza": "Europe/Zurich",
    "belgica": "Europe/Brussels",
    "polonia": "Europe/Warsaw",
    "grecia": "Europe/Athens",
    "noruega": "Europe/Oslo",
    "suecia": "Europe/Stockholm",
    "finlandia": "Europe/Helsinki",
    "ucrania": "Europe/Kyiv",
    "rumania": "Europe/Bucharest",
    "hungria": "Europe/Budapest",
    "austria": "Europe/Vienna",
    "dinamarca": "Europe/Copenhagen",

    # 🇺🇸 América
    "estados unidos": "America/New_York",
    "canada": "America/Toronto",
    "mexico": "America/Mexico_City",
    "brasil": "America/Sao_Paulo",
    "argentina": "America/Argentina/Buenos_Aires",
    "chile": "America/Santiago",
    "colombia": "America/Bogota",
    "peru": "America/Lima",
    "venezuela": "America/Caracas",
    "uruguay": "America/Montevideo",
    "paraguay": "America/Asuncion",
    "bolivia": "America/La_Paz",
    "ecuador": "America/Guayaquil",
    "cuba": "America/Havana",
    "republica dominicana": "America/Santo_Domingo",

    # 🌏 Asia
    "japon": "Asia/Tokyo",
    "china": "Asia/Shanghai",
    "corea del sur": "Asia/Seoul",
    "india": "Asia/Kolkata",
    "tailandia": "Asia/Bangkok",
    "singapur": "Asia/Singapore",
    "malasia": "Asia/Kuala_Lumpur",
    "indonesia": "Asia/Jakarta",
    "filipinas": "Asia/Manila",
    "pakistan": "Asia/Karachi",
    "bangladesh": "Asia/Dhaka",
    "arabia saudita": "Asia/Riyadh",
    "emiratos arabes unidos": "Asia/Dubai",
    "israel": "Asia/Jerusalem",
    "turquia": "Europe/Istanbul",

    # 🌍 África
    "sudafrica": "Africa/Johannesburg",
    "egipto": "Africa/Cairo",
    "nigeria": "Africa/Lagos",
    "kenia": "Africa/Nairobi",
    "etiopia": "Africa/Addis_Ababa",
    "marruecos": "Africa/Casablanca",
    "argelia": "Africa/Algiers",
    "ghana": "Africa/Accra",

    # 🌊 Oceanía
    "australia": "Australia/Sydney",
    "nueva zelanda": "Pacific/Auckland",
    "fiyi": "Pacific/Fiji"
}

if hora_ahora in zonas_horarias:
    zona_horaria = zonas_horarias[hora_ahora]
    hora_actual = datetime.now(ZoneInfo(zona_horaria))
    print(f"\nLa hora y fecha actual en la capital de {hora_ahora.title()} son")
    print(f"\n[+] Hora exacta: {hora_actual.strftime('%-I:%M %p')}")
    print(f"\n[+] Fecha exacta: {hora_actual.strftime('%d - %B - %Y')}") 
else:
    print("\nLo siento, no tengo información sobre ese país. Por favor, intenta con otro país.\n")

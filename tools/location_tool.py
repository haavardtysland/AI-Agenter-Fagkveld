from agents import function_tool

@function_tool
def search_location(city_name: str) -> str:
    """
    Search for a city's coordinates in our knowledge base.
    """
    print()  # Add spacing
    print("─" * 50)
    print(f"🔍 AGENTBESLUTNING: Søker koordinater for '{city_name}' i kunnskapsbase")
    
    # Kunnskapsdatabase med norske byer og koordinater
    # I en ekte applikasjon kunne dette vært en vektor database, SQL database, eller API
    CITY_COORDINATES = {
        "oslo": {"lat": 59.9139, "lon": 10.7522, "name": "Oslo"},
        "bergen": {"lat": 60.3913, "lon": 5.3221, "name": "Bergen"},
        "trondheim": {"lat": 63.4305, "lon": 10.3951, "name": "Trondheim"},
        "stavanger": {"lat": 58.9700, "lon": 5.7331, "name": "Stavanger"},
        "tromsø": {"lat": 69.65455, "lon": 18.96366, "name": "Tromsø"},
        "drammen": {"lat": 59.7439, "lon": 10.2045, "name": "Drammen"},
        "fredrikstad": {"lat": 59.2181, "lon": 10.9298, "name": "Fredrikstad"},
        "kristiansand": {"lat": 58.1467, "lon": 7.9956, "name": "Kristiansand"},
        "sandnes": {"lat": 58.8516, "lon": 5.7372, "name": "Sandnes"},
        "bodø": {"lat": 67.2804, "lon": 14.4040, "name": "Bodø"},
        "molde": {"lat": 62.7378, "lon": 7.1618, "name": "Molde"},
        "ålesund": {"lat": 62.4722, "lon": 6.1494, "name": "Ålesund"},
        "tønsberg": {"lat": 59.2674, "lon": 10.4073, "name": "Tønsberg"},
        "sarpsborg": {"lat": 59.2839, "lon": 11.1094, "name": "Sarpsborg"},
        "haugesund": {"lat": 59.4138, "lon": 5.2680, "name": "Haugesund"},
        "moss": {"lat": 59.4369, "lon": 10.6579, "name": "Moss"},
        "porsgrunn": {"lat": 59.1405, "lon": 9.6535, "name": "Porsgrunn"},
        "arendal": {"lat": 58.4617, "lon": 8.7722, "name": "Arendal"},
        "hamar": {"lat": 60.7945, "lon": 11.0680, "name": "Hamar"},
        "larvik": {"lat": 59.0537, "lon": 10.0387, "name": "Larvik"},
    }
    
    # Normalisere søkeordet til små bokstaver og fjern ekstra mellomrom
    search_key = city_name.lower().strip()
    
    if search_key in CITY_COORDINATES:
        result = CITY_COORDINATES[search_key]
        print(f"✅ KUNNSKAPSBASERT TREFF: Fant {result['name']} på lat={result['lat']}, lon={result['lon']}")
        return f"Fant {result['name']}: breddegrad {result['lat']}, lengdegrad {result['lon']}"
    else:
        print(f"❌ KUNNSKAPSBASERT BOM: '{city_name}' ikke funnet")
 
        return f"Beklager, jeg finner ikke koordinater for '{city_name}' i min kunnskapsbase. Prøv en annen by."

 
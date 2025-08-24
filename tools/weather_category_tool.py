"""
Foursquare Categories Tool
=========================
Returns relevant Foursquare category IDs for weather-based activity selection.
"""

from agents import function_tool


@function_tool
def get_foursquare_categories() -> str:
    """
    Get relevant Foursquare category IDs organized by activity type.
    Returns comma-separated category IDs that can be used directly in get_activities().
    """
    print()  # Add spacing
    print("─" * 50)
    print("🎯 AGENTBESLUTNING: Henter relevante Foursquare kategori-IDer")
    
    try:
        # Organize categories by activity type for easy weather-based selection
        indoor_categories = [
            "4bf58dd8d48988d17f941735",  # Movie Theaters
            "4d4b7104d754a06370d81259",  # Arts and Entertainment
            "4d4b7105d754a06374d81259",  # Restaurants
            "4bf58dd8d48988d116941735",  # Bars
            "13389",  # Irish Pub
            "4bf58dd8d48988d181941735",  # Museums
            "4bf58dd8d48988d18f941735",  # Art Galleries
            "4bf58dd8d48988d147941735",  # Bookstores
            "4bf58dd8d48988d1e5931735",  # Coffee Shops
        ]
        
        outdoor_categories = [
            "4bf58dd8d48988d163941735",  # Parks
            "4bf58dd8d48988d164941735",  # Beaches
            "4bf58dd8d48988d15f941735",  # Harbors / Marinas
            "4bf58dd8d48988d162941735",  # Trails
            "4bf58dd8d48988d161941735",  # Gardens
            "4bf58dd8d48988d165941735",  # Scenic Lookouts
            "4bf58dd8d48988d160941735",  # Piers
            "16055",  # Boat Launch
            "18086",  # Fishing Area
        ]
        
        sports_recreation = [
            "4bf58dd8d48988d175941735",  # Gym and Studios
            "18077",  # Gym and Studio > Gym
            "4bf58dd8d48988d15e941735",  # Swimming Pools
            "4bf58dd8d48988d1e9941735",  # Ski Resorts and Areas
            "58daa1558bbb0b01f18ec1ae",  # Saunas
            "4bf58dd8d48988d1f4931735",  # Race Tracks
            "10057",  # Disc Golf
        ]
        
        response = "Foursquare kategori-IDer for aktivitetssøk:\n\n"
        response += f"INNENDØRS: {','.join(indoor_categories)}\n"
        response += f"UTENDØRS: {','.join(outdoor_categories)}\n"
        response += f"SPORT/REKREASJON: {','.join(sports_recreation)}\n\n"
        response += "Bruk disse IDene direkte i get_activities() med categories parameter.\n"
        response += "Eksempel: get_activities(lat, lon, categories=\"4bf58dd8d48988d163941735,4bf58dd8d48988d164941735\")"
        
        total_categories = len(indoor_categories) + len(outdoor_categories) + len(sports_recreation)
        print(f"✅ KATEGORIER: Returnerte {total_categories} kategori-IDer organisert etter type")
        return response
        
    except Exception as e:
        print(f"❌ KATEGORIFEIL: {str(e)}")
        return f"Kunne ikke hente kategorier: {str(e)}" 
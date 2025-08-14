"""
Activities Tool
===============
Get activity suggestions for given coordinates.
"""

import os

import requests
from agents import function_tool


@function_tool
def get_activities(lat: float, lon: float, query: str = "things to do", categories: str = None, limit: int = 5) -> str:
    """
    Get activity suggestions for given coordinates.
    
    Args:
        lat: Latitude coordinates
        lon: Longitude coordinates
        query: Search query for types of activities (e.g., "outdoor activities", "museums", "restaurants")
        categories: Comma-separated Foursquare category IDs (e.g., "4bf58dd8d48988d17f941735,4d4b7105d754a06374d81259")
        limit: Maximum number of activities to return (default 5)
    """
    print()  # Add spacing
    print("─" * 50)
    if categories:
        print(f"🎯 AGENTBESLUTNING: Søker etter aktiviteter med categories='{categories}' på koordinater ({lat}, {lon}), limit={limit}")
    else:
        print(f"🎯 AGENTBESLUTNING: Søker etter aktiviteter med query='{query}' på koordinater ({lat}, {lon}), limit={limit}")
    
    api_key = os.environ.get("FOURSQUARE_API_KEY")
    if not api_key:
        return "API-nøkkel mangler. Sett FOURSQUARE_API_KEY i miljøvariabler."
    
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": api_key,
    }
    params = {
        "ll": f"{lat},{lon}",
        "limit": limit,
        "sort": "RELEVANCE"
    }
    
    # Use categories if provided, otherwise use query
    if categories:
        params["categories"] = categories
        search_type = f"categories '{categories}'"
    else:
        params["query"] = query
        search_type = f"query '{query}'"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        
        print(f"🔍 API-FORESPØRSEL: {url} med params: {params}")
        print(f"📊 API-SVAR: Fikk {len(results)} resultater fra API")
        
        if not results:
            print(f"❌ TOMT SVAR: API returnerte ingen resultater for {search_type}")
            return f"Fant ingen aktiviteter for {search_type}."
        
        activities = []
        for place in results:
            name = place.get("name", "Ukjent sted")
            # Fix: handle both string and list formats for address
            location = place.get("location", {})
            address = ""
            
            if "formatted_address" in location:
                formatted_addr = location["formatted_address"]
                if isinstance(formatted_addr, list):
                    address = ", ".join(formatted_addr)
                elif isinstance(formatted_addr, str):
                    address = formatted_addr
                else:
                    address = "Adresse ikke tilgjengelig"
            else:
                # Fallback to constructing address from components
                addr_parts = []
                if "address" in location:
                    addr_parts.append(location["address"])
                if "locality" in location:
                    addr_parts.append(location["locality"])
                address = ", ".join(addr_parts) if addr_parts else "Adresse ikke tilgjengelig"
            
            activities.append(f"{name} ({address})")
        
        print(f"✅ API-SVAR: Hentet {len(activities)} aktiviteter for {search_type}")
        return "Forslag til aktiviteter: " + "; ".join(activities)
        
    except Exception as e:
        print(f"❌ API-FEIL: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"📄 HTTP-STATUS: {e.response.status_code}")
            print(f"📄 HTTP-SVAR: {e.response.text[:200]}...")
        return f"Kunne ikke hente aktiviteter: {str(e)}"


 
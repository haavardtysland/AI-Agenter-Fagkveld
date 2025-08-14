"""
Weather Tool
============
Get current weather data from the Norwegian Meteorological Institute (YR API)
"""

from datetime import datetime

import requests
from agents import function_tool


@function_tool
def get_weather(lat: float, lon: float, location_name: str = None) -> str:
    """
    Get current weather data from the Norwegian Meteorological Institute (YR API)
    
    Args:
        lat: Latitude coordinates
        lon: Longitude coordinates  
        location_name: Optional name of the location for context
    """
    print()  # Add spacing
    print("─" * 50)
    print(f"🌤️ AGENTBESLUTNING: Henter værdata for {location_name or f'koordinater {lat}, {lon}'} (lat={lat}, lon={lon})")
    
    try:
        # Round coordinates as required by YR API
        lat = round(float(lat), 4)
        lon = round(float(lon), 4)
        
        # Call the YR API - using compact version for simplicity
        url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
        headers = {"User-Agent": "WeatherAgent/1.0"}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Get the first (current/closest) forecast entry
        current_weather = data["properties"]["timeseries"][0]
        
        # Extract basic weather info
        instant = current_weather["data"]["instant"]["details"]
        temp = instant["air_temperature"]
        
        # Get precipitation info from next hour if available
        precipitation_amount = 0
        precipitation_probability = 0
        
        if "next_1_hours" in current_weather["data"]:
            details = current_weather["data"]["next_1_hours"].get("details", {})
            precipitation_amount = details.get("precipitation_amount", 0)
            precipitation_probability = details.get("probability_of_precipitation", 0)
        
        forecast_time = current_weather["time"]
        location_str = f" i {location_name}" if location_name else ""
        
        print(f"✅ YR API-SVAR: {temp}°C, nedbør: {precipitation_amount}mm ({precipitation_probability}% sannsynlighet) for {forecast_time}")
        
        return f"Vær{location_str} ({forecast_time}): {temp}°C, nedbør neste time: {precipitation_amount}mm (sannsynlighet: {precipitation_probability}%)"
        
    except Exception as e:
        print(f"❌ Feil ved henting av værdata: {str(e)}")
        return f"Kunne ikke hente værdata: {str(e)}"


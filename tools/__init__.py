"""
Tools Package
=============
Modular tools for the Norwegian Weather Agent.

Each tool can be tested independently by running the individual tool files:
- python tools/weather_tool.py
- python tools/activities_tool.py  
- python tools/location_tool.py

Or import them into other modules:
 - from tools.weather_tool import get_weather
- from tools.activities_tool import get_activities
  - from tools.location_tool import search_location
"""

from weather_category_tool import get_foursquare_categories

from .activities_tool import get_activities
from .location_tool import search_location
from .weather_tool import get_weather

# Export everything for easy imports
__all__ = [
    # Functions
    'get_weather',
    'get_activities', 
    'search_location',
    'get_foursquare_categories'
] 
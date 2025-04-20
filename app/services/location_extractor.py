import re
import geonamescache

gc = geonamescache.GeonamesCache()
all_cities = [re.escape(city['name'].lower()) for city in gc.get_cities().values()]  # escape special characters

# Compile a single regex pattern for all cities (faster than looping)
city_pattern = re.compile(r'\b(' + '|'.join(all_cities) + r')\b', re.IGNORECASE)

def extract_city_from_text(text: str) -> str | None:
    match = city_pattern.search(text.lower())
    return match.group(0).title() if match else None

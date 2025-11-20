# Write code to fetch weather data from a public API using Python requests.
import requests
def fetch_weather_data(city):
    api_key = 'your_api_key_here'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    # --- Review Notes ---

# Security Risk 1: API key is hard-coded in the source code.
# Problem: If this file is pushed to GitHub, the API key can be stolen.
# Mitigation: Store API keys in environment variables or a .env file.

# Security Risk 2: No timeout or error handling in the request.
# Problem: API may hang, fail silently, or return errors.
# Mitigation: Add timeout=5, check status codes, use try/except blocks.

# Licensing Risk: Copilot may use code patterns from libraries with restrictive licenses.
# Problem: This may violate GPL or proprietary licenses if copied.
# Mitigation: Verify the source of code, and use official API documentation instead.
    }
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    return params
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    return params
    




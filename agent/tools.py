import datetime
import requests

def get_live_weather_forecast(location: str) -> str:
    """
    Gets the live weather forecast for a given location.

    Args:
        location: The location to get the weather forecast for.

    Returns:
        The weather forecast for the given location.
    """
    try:
        # First, get the coordinates for the location using the NWS API
        url = f"https://api.weather.gov/points/{location}"
        response = requests.get(url)
        response.raise_for_status()
        grid_id = response.json()["properties"]["gridId"]
        grid_x = response.json()["properties"]["gridX"]
        grid_y = response.json()["properties"]["gridY"]

        # Now, get the forecast using the grid information
        url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"
        response = requests.get(url)
        response.raise_for_status()
        forecast = response.json()["properties"]["periods"][0]
        return f"The weather in {location} is {forecast['temperature']}°{forecast['temperatureUnit']} and {forecast['shortForecast']}"
    except requests.exceptions.RequestException as e:
        return f"Could not get weather for {location}: {e}"


def get_current_time(location: str) -> str:
    """
    Gets the current time for a given location.

    Args:
        location: The location to get the current time for.

    Returns:
        The current time for the given location.
    """
    # This is a simplified implementation and does not handle timezones.
    # A more robust implementation would use a library like pytz.
    now = datetime.datetime.now()
    return f"The current time in {location} is {now.strftime('%H:%M:%S')}"

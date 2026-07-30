import httpx


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


async def get_coordinates(city: str):

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "ru",
                "format": "json",
            },
        )

    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None

    place = data["results"][0]

    return {
        "name": place["name"],
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "timezone": place.get("timezone", "Europe/Moscow"),
    }


async def get_current_weather(latitude: float, longitude: float):

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "timezone": "auto",
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "apparent_temperature",
                    "wind_speed_10m",
                    "weather_code",
                ],
                "daily": [
                    "temperature_2m_max",
                    "temperature_2m_min",
                    "precipitation_probability_max",
                    "sunrise",
                    "sunset",
                ],
                "forecast_days": 1,
                "wind_speed_unit": "ms",
            },
        )

    response.raise_for_status()

    return response.json()


async def get_week_weather(latitude: float, longitude: float):

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            FORECAST_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "timezone": "auto",
                "daily": [
                    "weather_code",
                    "temperature_2m_max",
                    "temperature_2m_min",
                    "precipitation_probability_max",
                ],
                "forecast_days": 7,
            },
        )

    response.raise_for_status()

    return response.json()
import httpx


async def get_coordinates(city: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            url,
            params={
                "name": city,
                "count": 1,
                "language": "ru",
                "format": "json",
            },
        )

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
    url = "https://api.open-meteo.com/v1/forecast"

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            url,
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
                    "sunrise",
                    "sunset",
                ],
                "forecast_days": 1,
                "wind_speed_unit": "ms",
            },
        )

    return response.json()
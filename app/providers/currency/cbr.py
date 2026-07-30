import httpx
from datetime import datetime


CBR_URL = "https://www.cbr-xml-daily.ru/daily_json.js"


async def get_rates():

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(CBR_URL)

    response.raise_for_status()

    json_data = response.json()

    data = json_data["Valute"]

    def rate(code: str):
        item = data[code]
        return item["Value"] / item["Nominal"]

    updated = datetime.fromisoformat(
        json_data["Date"].replace("Z", "+00:00")
    )

    return {
        "updated": updated.strftime("%d.%m.%Y %H:%M"),
        "USD": round(rate("USD"), 2),
        "EUR": round(rate("EUR"), 2),
        "CNY": round(rate("CNY"), 2),
        "KZT": round(rate("KZT"), 2),
    }
from app.providers.currency.cbr import get_rates


async def convert(amount: float, from_currency: str):
    """
    Конвертация из любой валюты
    во все остальные.
    """

    rates = await get_rates()

    # Курс каждой валюты к рублю
    rub_rates = {
        "RUB": 1.0,
        "USD": rates["USD"],
        "EUR": rates["EUR"],
        "CNY": rates["CNY"],
        "KZT": rates["KZT"],
    }

    from_currency = from_currency.upper()

    if from_currency not in rub_rates:
        raise ValueError(f"Неизвестная валюта: {from_currency}")

    # Сначала переводим всё в рубли
    rub = amount * rub_rates[from_currency]

    # Затем из рублей во все валюты
    return {
        "RUB": round(rub, 2),
        "USD": round(rub / rub_rates["USD"], 2),
        "EUR": round(rub / rub_rates["EUR"], 2),
        "CNY": round(rub / rub_rates["CNY"], 2),
        "KZT": round(rub / rub_rates["KZT"], 2),
    }
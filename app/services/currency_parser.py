import re


CURRENCY_ALIASES = {
    "RUB": [
        "руб",
        "руб.",
        "рубль",
        "рублей",
        "₽",
        "rub",
    ],

    "USD": [
        "$",
        "usd",
        "доллар",
        "доллара",
        "долларов",
    ],

    "EUR": [
        "€",
        "eur",
        "евро",
    ],

    "CNY": [
        "¥",
        "cny",
        "юань",
        "юаня",
        "юаней",
    ],

    "KZT": [
        "₸",
        "kzt",
        "тенге",
    ],
}


def parse_currency(text: str):

    text = text.lower().strip()

    text = (
        text.replace(",", ".")
            .replace("₽", " ₽ ")
            .replace("$", " $ ")
            .replace("€", " € ")
            .replace("¥", " ¥ ")
            .replace("₸", " ₸ ")
    )

    text = re.sub(r"\s+", " ", text)

    match = re.search(r"(\d[\d\s]*\.?\d*)", text)

    if not match:
        return None

    amount = (
        match.group(1)
        .replace(" ", "")
    )

    amount = float(amount)

    for code, aliases in CURRENCY_ALIASES.items():

        for alias in aliases:

            if alias in text:
                return amount, code

    return None
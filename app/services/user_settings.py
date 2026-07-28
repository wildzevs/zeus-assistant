user_cities = {}


def set_city(user_id: int, city: str):
    user_cities[user_id] = city


def get_city(user_id: int):
    return user_cities.get(user_id)
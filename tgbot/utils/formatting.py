from tgbot.models.house import House


def house_format(house: House) -> str:
    return f'Дом {house.start_house} - {house.end_house}'

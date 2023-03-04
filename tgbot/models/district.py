from enum import Enum


class DistrictEnum(str, Enum):
    ZAELTSOVSKY = 'Заельцовский'
    KALININSKY = 'Калининский'
    CENTRAL = 'Центральный'
    DZERZHINSKY = 'Дзержинский'
    OCTOBER = 'Октябрьский'
    LENINSKY = 'Ленинский'
    KIROVSKY = 'Кировский'
    MAYDAY = 'Первомайский'
    SOVIET = 'Советский'
    RAILWAY = 'Железнодорожный'

    @classmethod
    def list(cls):
        return list(map(lambda item: item.value, cls))

class DxOutOfRange(Exception):
    def __str__(self):
        return 'dx is out of range'


class DyOutOfRange(Exception):
    def __str__(self):
        return 'dy is out of range'


class NOutOfRange(Exception):
    def __str__(self):
        return 'n is out of range'


class QOutOfRange(Exception):
    def __str__(self):
        return 'q is out of range'


class ShopCoordinatesOutOfRange(Exception):
    def __init__(self, shop):
        self.shop = shop

    def __str__(self):
        return "Coordinates of shop {0} are out of range".format(self.shop)


class DistanceOutOfRange(Exception):
    def __str__(self):
        return 'disatance is out of range'


class DublicateShops(Exception):
    def __init__(self, position):
        self.position = position

    def __str__(self):
        return "dublicate shops at position: {0}".format(self.position)
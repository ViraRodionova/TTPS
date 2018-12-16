from Errors import DublicateShops


class City:
    def __init__(self, dx, dy):
        self.matrix = [[0] * dx for x in range(dy)]
        self.shops = []

    def __str__(self):
        res = 'City:\n'
        for x in range(len(self.matrix)):
            res += "{0}\n".format(self.matrix[x])

        # res += '\nShops:\n'
        #
        # for x in range(len(self.shops)):
        #     res += "{0}\n".format(self.shops[x])

        return res

    def add_shop(self, x, y):
        for shop in self.shops:
            if shop[0] == x and shop[1] == y:
                raise DublicateShops([x, y])

        self.shops.append([x, y])

    def get_number_of_shops_for_position(self, x, y, distance):
        res = 0
        for [c1, c2] in self.shops:
            if x == c1 and y == c2:
                return -1

            d = abs(x - c1) + abs(y - c2)

            if d > 0 and d <= distance:
                res += 1

        return res

    def calculate_shops(self, distance):
        _dx = len(self.matrix)
        _dy = len(self.matrix[0])

        for i in range(_dx):
            for j in range(_dy):
                self.matrix[i][j] = self.get_number_of_shops_for_position(i, j, distance)

    def get_best_positions(self, distance):
        self.calculate_shops(distance)

        res = []
        _max = 0

        _dx = len(self.matrix)
        _dy = len(self.matrix[0])

        for i in range(_dx):
            for j in range(_dy):
                _tmp = self.matrix[i][j]
                if _tmp > _max:
                    _max = _tmp
                    res = [[i + 1, j + 1]]
                elif _tmp == _max:
                    res.append([i + 1, j + 1])

        return [_max, res]

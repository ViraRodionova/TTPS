from Utils import *
from Errors import *
from City import City

DX_MIN = 1
DX_MAX = 1000
DY_MIN = 1
DY_MAX = 1000
N_MIN = 0
N_MAX = 105
Q_MIN = 1
Q_MAX = 20
M_MIN = 0
M_MAX = 106


def main(filename):
    shops = {}
    content = load_content(filename)
    i = 0

    c = get_string(content, i)

    dx = int(c[0])
    dy = int(c[1])
    n = int(c[2])
    q = int(c[3])

    # print dx, dy, n, q

    if dx < DX_MIN or dx > DX_MAX:
        raise DxOutOfRange()

    if dy < DY_MIN or dy > DY_MAX:
        raise DyOutOfRange()

    if n < N_MIN or n > N_MAX:
        raise NOutOfRange()

    if q < Q_MIN or q > Q_MAX:
        raise QOutOfRange()

    i += 1

    city = City(dx, dy)

    while i <= n and i < len(content):
        c = get_string(content, i)
        x = int(c[0])
        y = int(c[1])

        if x < 1 or x > dx or y < 1 or y > dy:
            raise ShopCoordinatesOutOfRange(i)

        x -= 1
        y -= 1

        city.add_shop(x, y)

        i += 1

    while i <= n + q and i < len(content):
        if len(get_string(content, i)) != 1:
            raise Exception()

        distance = int(get_string(content, i)[0])
        if distance < M_MIN or distance > M_MAX:
            raise DistanceOutOfRange()

        res = city.get_best_positions(distance)

        shops[distance] = {
            'shops': res[0],
            'positions': res[1]
        }

        # print '-' * 50
        # print 'Distance: ', distance
        # print 'Shops: ', res[0]
        # print 'Positions: ', res[1]

        # print city

        i += 1

    return shops


# shops = main('inputs/input3')

# print shops

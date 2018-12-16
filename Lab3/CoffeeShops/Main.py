from Utils import *
from City import City


def main(filename):
    shops = {}
    content = load_content(filename)
    i = 0

    c = get_string(content, i)

    dx = int(c[0])
    dy = int(c[1])
    n = int(c[2])
    q = int(c[3])

    i += 1

    city = City(dx, dy)

    while i <= n and i < len(content):
        c = get_string(content, i)
        x = int(c[0]) - 1
        y = int(c[1]) - 1

        city.add_shop(x, y)

        i += 1

    while i <= n + q and i < len(content):
        distance = int(get_string(content, i)[0])
        res = city.get_best_positions(distance)

        shops[distance] = {
            'shops': res[0],
            'positions': res[1]
        }

        print '-' * 50
        print 'Distance: ', distance
        print 'Shops: ', res[0]
        print 'Positions: ', res[1]

        print city

        i += 1

    return shops


shops = main('inputs/input1')

print shops

def calculate_area(base, height):
    area = (base * height) / 2

    print('The base of triangle is ' + str(area))


def run():
    print('Calculate area of triangle')

    base = int(input('Entry the base: '))
    height = int(input('Entry the height: '))

    calculate_area(base, height)


if __name__ == "__main__":
    run()


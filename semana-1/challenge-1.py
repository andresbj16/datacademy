def calculate_area(base, height):
    area = (base * height) / 2

    print(f'The base of triangle is {area}')


def run():
    print('Calculate area of triangle')

    try:
        base = int(input('Entry the base: '))
        height = int(input('Entry the height: '))
        calculate_area(base, height)
    except ValueError:
        print('You must entry a number\n')
        run()


if __name__ == "__main__":
    run()


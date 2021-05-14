MILE = 1.609344

def convert(convert_to, distance):
    try:
        assert str(convert_to).isnumeric(), 'You must entry some next options [1] Kilometers to Miles - [2] Miles to Kilometers'
        assert str(distance).isnumeric(), 'You must entry a number'

        distance = float(distance)
        if(convert_to == '1'):
            print(str(distance) + ' kilometers are ' + str(distance / MILE))
        elif(convert_to == '2'):
            print(str(distance) + ' miles are ' + str(MILE * distance))
        else:
            print('Option is not valid')
    except AssertionError as ae:
        print(ae)


def run():
    convert_to = input('''
Converter of miles and kilometers

[1] Kilometers to Miles
[2] Miles to Kilometers

What type conversion do you want? ''')

    distance = input('Entry distance: ')

    convert(convert_to, distance)


if __name__ == '__main__':
    run()
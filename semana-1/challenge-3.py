MILE = 1.609344

def convert(convert_to, distance):
    distance = float(distance)
    if(convert_to == '1'):
        print(str(distance) + ' kilometers are ' + str(distance / MILE))
    elif(convert_to == '2'):
        print(str(distance) + ' miles are ' + str(MILE * distance))
    else:
        print('Option is not valid')


def run():
    convert_to = input('''
Converter of miles and kilometers

What type conversion do you want?

[1] Kilometers to Miles
[2] Miles to Kilometers

''')

    distance = input('Entry distance: ')

    convert(convert_to, distance)


if __name__ == '__main__':
    run()
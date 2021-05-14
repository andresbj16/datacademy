def change_range(lower_limit, hight_limit, comparasion_value):
    lower_limit = int(lower_limit)
    hight_limit = int(hight_limit)
    comparasion_value = int(comparasion_value)

    if (comparasion_value >= lower_limit and comparasion_value <= hight_limit):
        print('Comparasion value ' + str(comparasion_value) + ' between limits ' + str(lower_limit) + ' and ' + str(hight_limit))
    else:
        print('Comparasion value ' + str(comparasion_value) + ' out limits ' + str(lower_limit) + ' and ' + str(hight_limit))

        if (comparasion_value < lower_limit):
            lower_limit = comparasion_value
        elif (comparasion_value > hight_limit):
            hight_limit = comparasion_value

        print('\nCurrent lower limit: '+ str(lower_limit))
        print('Current hight limit: '+ str(hight_limit))
        comparasion_value = comparasion_value = input('Entry the comparasion value: ')
        change_range(lower_limit, hight_limit, comparasion_value)


def run():
    figure = print('''
Change Of Range

Entry three numbers
''')

    lower_limit = input('Entry the lower limit: ')
    hight_limit = input('Entry the hight limit: ')
    comparasion_value = input('Entry the comparasion value: ')

    change_range(lower_limit, hight_limit, comparasion_value)

if (__name__ == '__main__'):
    run()
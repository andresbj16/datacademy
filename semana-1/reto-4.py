import math

def calcule_cylinder(radius, height):
    volume = (math.pi * math.pow(radius, 2) * height)
    print('The volume of cylinder is: ' + str(volume))


def calcule_cube(length, height, width):
    volume = length * height * width
    print('The volume of cube is: ' + str(volume))


def calcule_prism(length, height, width):
    volume = 1/2 * length * height * width
    print('The volume of prism is: ' + str(volume))


def cylinder():
    radius = float(input('Entry radius: '))
    height = float(input('Entry height: '))
    calcule_cylinder(radius, height)

def cube():
    length = float(input('Entry length: '))
    height = float(input('Entry height: '))
    width = float(input('Entry width: '))
    calcule_cube(length, height, width)


def prism():
    length = float(input('Entry length: '))
    height = float(input('Entry height: '))
    width = float(input('Entry width: '))
    calcule_prism(length, height, width)


def determine_figure(figure):
    if(figure == '1'):
        cylinder()
    elif (figure == '2'):
        cube()
    elif (figure == '3'):
        prism()


def run():
    figure = input('''
Volume Figure Calculate

What volume figure do you want to get?

[1] Cylinder
[2] Cube
[3] Prism

''')

    determine_figure(figure)


if (__name__ == '__main__'):
    run()

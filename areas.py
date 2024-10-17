class triangle:
    def __init__(self, h, b):
        self.base = b
        self.height = h
    def area(self):
        self.area = self.base * self.height * 0.5
        print('your triangle area is: ' f"{self.area: .2f}" )

class circle:
    def radius(self):
        self.radius = float(input('enter radius: '))
    def area(self):
        from math import pi
        self.area = self.radius ** 2 * round(pi , 4)
        print('your circle area is: ', f"{self.area: .2f}")

class rhombus:
    def __init__(self, h, b):
        self.base = b
        self.height = h
    def area(self):
        self.area = self.base * self.height
        print('your rhombus area is: ' f"{self.area: .2f}" )
        
class trapzoid:
    def __init__(self , b1, b2, h):
        self.base1 = b1
        self.base2 = b2
        self.height = h
    def area(self):
        self.area = self.height * (self.base1 + self.base2) / 2
        print('your rhombus area is: ' f"{self.area: .2f}" )

print(
    'pls choose your need... \n A for trinagle. \n B for circle. \n C for rhombus. \n D for trapzoid.'
)
draw_list = ['a', 'b', 'c', 'd']
get_draw = input('Type what you need: ').lower()
if get_draw not in draw_list:
    print('response not founded...')
if get_draw == 'a':
    height = float(input('please inter the height: '))
    base = float(input('pls inter the base: '))
    my_triangle = triangle(height, base)
    my_triangle.area()
if get_draw == 'b':
    my_circle = circle()
    my_circle.radius()
    my_circle.area()
if get_draw == 'c':
    height = float(input('please inter the height: '))
    base = float(input('pls inter the base: '))
    my_rhombus = rhombus(height, base)
    my_rhombus.area()
if get_draw == 'd':
    height = float(input('please inter the height: '))
    base1= float(input('pls inter the top base: '))
    base2 = float(input('pls inter bottom base: '))
    my_trapzoid = trapzoid(height, base1, base2)
    my_trapzoid.area()
import math

class Room:
    """
    Прямоугольная площадка (пример: комната) (свойства: две стороны).
    Методы:
    1. вычисляем площадь,
    2. вычисляем периметр.
    """

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def room_area(self):
        return self.length * self.width

    def room_perimeter(self):
        return 2 * (self.length + self.width)

class Decart_Point:
    """
    Точка на карте (свойства: X, Y).
    Методы:
    1. Нужно вычислить расстояние до начала координат,
    2. * вычисляется расстояние между точкой и другой точкой экземпляром этого же
    класса
    3. ** перевод в другие системы координат
    """

    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y

    def distance_origin(self):
        # return self.distance_two_dots(Decart_Point(0,0))
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return '[{}, {}]'.format(self.x, self.y)

    def distance_two_dots(self, dot2):
        return math.sqrt((self.x - dot2.x) ** 2 + (self.y - dot2.y) ** 2)

    def decart_to_polar(self):
        """
        положение точки P определяется её расстоянием до начала координат r = |OP|
        и углом φ её радиус-вектора к оси Ox.
        """
        length = self.distance_origin()
        radian = math.atan2(self.y, self.x)
        self.x, self.y = length, radian

    def polar_to_decart(self):
        """
        пересчет из полярных координат в декартовы
        """
        xval = self.x * math.cos(self.y)
        yval = self.x * math.sin(self.y)
        self.x, self.y = xval, yval


if __name__ == '__main__':
#
    kitchen = Room(width=3, length=4)
    print('Kitchen area is', kitchen.room_area())
    print('Kitchen perimeter is', kitchen.room_perimeter())
#
    dot1 = Decart_Point(5, 12)
    dot2 = Decart_Point(-12, 3)
    print('точка {}: расстояние до начала координат = {}'.format(str(dot1), dot1.distance_origin()))
    print('точка {}: расстояние до точки {} = {}'.format(str(dot1), str(dot2), dot1.distance_two_dots(dot2)))
    print('Расстояние в другую сторону такое же = {}'.format(dot2.distance_two_dots(dot1)))
    print('Декартовы координаты точки = {}'.format(str(dot2)))
    dot2.decart_to_polar()
    print('Полярные координаты точки = {}'.format(str(dot2)))
    dot2.polar_to_decart()
    print('И снова декартовы координаты точки = {}'.format(str(dot2)))

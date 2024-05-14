class GeometricObject:
    """
    Class of geometric object
    """

    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        """
        :param x: x coordinate
        :param y: y coordinate
        :param color: color
        :param filled: status filled
        """

        if isinstance(x, int | float):
            self.__x = float(x)
        else:
            self.__x = 0.0

        if isinstance(y, int | float):
            self.__y = float(y)
        else:
            self.__y = 0.0

        if isinstance(color, str):
            self.color = color
        else:
            self.color = 'black'

        if isinstance(filled, bool):
            self.filled = filled
        else:
            self.filled = False

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def set_coordinate(self, new_x, new_y):
        if isinstance(new_x, int | float):
            self.__x = float(new_x)
        else:
            self.__x = 0.0

        if isinstance(new_y, int | float):
            self.__y = float(new_y)
        else:
            self.__y = 0.0

    def set_color(self, new_color):
        if isinstance(new_color, str):
            self.color = new_color
        else:
            self.color = 'black'

    def set_filled(self, new_filled):
        if isinstance(new_filled, bool):
            self.filled = new_filled
        else:
            self.filled = False

    def __str__(self):
        return f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        if self.is_filled():
            status = 'filled'
        else:
            status = 'no filled'

        return f'{int(self.get_x())},{int(self.get_y())} {self.get_color()} {status}'


class Rectangle(GeometricObject):
    """
    Class of rectangle.
    """

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)

        if isinstance(width, int | float) and width > 0:
            self.width = float(width)
        else:
            self.width = 0.0

        if isinstance(height, int | float) and height > 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def set_width(self, new_width):
        if isinstance(new_width, int | float) and new_width > 0:
            self.width = float(new_width)
        else:
            self.width = 0.0

    def set_height(self, new_height):
        if isinstance(new_height, int | float) and new_height > 0:
            self.height = float(new_height)
        else:
            self.height = 0.0

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'width: {self.get_width()}\n' \
               f'height: {self.get_height()}\n'\
               f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        if self.is_filled():
            status = 'filled'
        else:
            status = 'no filled'

        return f'width:{int(self.get_width())}, height:{int(self.get_height())}' \
               f' ({int(self.get_x())},{int(self.get_y())}) {self.get_color()}' \
               f' {status}'


class Circle(GeometricObject):
    PI = 3.1415926535
    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if isinstance(radius, int | float) and radius > 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, int | float) and value > 0:
            self.__radius = float(value)
        else:
            self.__radius = 0.0

    def get_area(self):
        return Circle.PI * self.radius ** 2

    def get_perimetr(self):
        return 2 * Circle.PI * self.radius

    def get_diametr(self):
        return 2 * self.radius

    def __str__(self):
         return f'radius: {self.radius}\n'\
               f'({self.get_x()}, {self.get_y()})\n' \
               f'color: {self.get_color()}\n' \
               f'filled: {self.is_filled()}\n'

    def __repr__(self):
        if self.is_filled():
            status = 'filled'
        else:
            status = 'no filled'

        return f'radius:{int(self.radius)} ({int(self.get_x())},' \
               f'{int(self.get_y())}) {self.get_color()} {status}'
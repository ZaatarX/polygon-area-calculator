import math


class Rectangle:
    def __init__(self, width, height) -> None:
        self.set_width(width)
        self.set_height(height)

    def __str__(self) -> str:
        return f'Rectangle(width={self.get_width()}, height={self.get_height()})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return 2 * self.get_width() + 2 * self.get_height()

    def get_diagonal(self):
        return (self.get_width() ** 2 + self.get_height() ** 2) ** .5

    def get_picture(self):
        if self.get_width() <= 50 and self.get_height() <= 50:
            picture = ''
            for value in range(0, self.get_height()):
                picture += '*' * self.get_width() + '\n'
            return picture

        return "Too big for picture."

    def get_amount_inside(self, shape):
        return math.floor(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, length) -> None:
        self.set_side(length)

    def __str__(self) -> str:
        return f'Square(side={self.get_side()})'

    def set_side(self, length):
        super().__init__(length, length)

    def get_side(self):
        return super().get_width()

from math import sqrt
from random import randint

#A circle class to hold all of the points within its boundaries
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.radius = r

    def __repr__(self):
        return ("A circle centered at %i, %i, with a radius of %.1f"
                % (self.x, self.y, self.radius))

    def dist(self, point):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

    def contains(self, point):
        return self.dist(point) < self.radius

#A Point class to keep track of generated x and y coordinates.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ("A point located at %i, %i" % (self.x, self.y))

#A Square class to contain all the points in a given space
class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return ("A %i by %i square located at %.1f, %.1f"
                % (self.width, self.height, self.x, self.y))

#A default square and circle to start with
sq = Square(0, 0, 100, 100)
ci = Circle(50, 50, 50)

#Find pi using the monte carlo method with a square and circle
#Returns an approximation of pi by dividing the number of points within
#a circle by the number of points within the square.
def findPi(square=sq, circle=ci, loops=7e5):
    if (not circle.radius == square.width/2 or
        not circle.radius == square.height/2):
        print('Square and Circle are of mismatched sizes.')
        return
    if (not circle.x == square.x + square.width / 2 or
        not circle.y == square.y + square.height / 2):
        print('The circle is not in the correct location to get the proper result.')
        return
    index = 0
    pointsWithin = 0
    totalPoints = 0
    while index < loops:
        x = randint(square.x, square.x + square.width) + 1
        y = randint(square.y, square.y + square.height) + 1
        point = Point(x, y)
        if circle.contains(point):  pointsWithin += 1
        totalPoints += 1
        index += 1
    return (pointsWithin / totalPoints) * 4

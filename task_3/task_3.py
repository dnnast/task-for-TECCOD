# Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.

import math
import numbers

class Point:
    def __init__(self, x, y):
        self.checkInputValues(x,y)
       
        self.x = x
        self.y = y

    def measureDist(self, x2, y2):
        self.checkInputValues(x2,y2)
        
        return math.sqrt( (x2 - self.x)**2 + (y2 - self.y)**2 )

    def changeCoord(self, x_new, y_new):
        self.checkInputValues(x_new,y_new)

        self.x = x_new
        self.y = y_new

    def printCoord(self):     
        print("x: {}\ny: {}".format(self.x, self.y))

    def checkInputValues(self, x, y):
        if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
            raise ValueError("Invalid input. Both '{}' and '{}' values have to be numbers".format(x,y))

if __name__ == '__main__':

    point = Point(2,4)   
    print(point.measureDist(4,5))  
    point.printCoord()
    point.changeCoord(8,7)   
    print(point.measureDist(4,5))  
    point.printCoord()

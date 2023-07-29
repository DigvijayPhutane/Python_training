from abc import ABC , abstractmethod
class polygon(ABC):
    def noofside(self):
        pass
class triangle(polygon):
    def noofside(self):
        print("3 sides")
class pentagon(polygon):
    def noofside(self):
        print("5 sides")
class hexagon(polygon):
    def noofside(self):
        print("6 side")
r = triangle()
r.noofside()

k = pentagon()
k.noofside()

s = hexagon()
s.noofside()
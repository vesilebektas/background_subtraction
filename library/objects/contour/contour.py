from library.objects.image.image import Image
from library.objects.color.color import Color
from library.objects.threshold.threshold import Thresh
import cv2


class Contour:
    def __init__(self, image: Image):
        self.__image = image
        self.__contours = None
        self.__hierarchy = None
        self.__contour = None
        self.__hierarchy_index = None

    def set_contours(self, contours: list):
        self.__contours = contours
        return self

    def find(self):
        self.__contours, self.__hierarchy = cv2.findContours(self.__image.get(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return self

    def get_contours(self):
        return self.__contours

    def get_hierarchy(self):
        return self.__hierarchy


class Filter:
    def __init__(self, contour: Contour):
        self.__contour = contour

    def filter_by_area(self, min_area: int = 0, max_area: int = 1000):
        contours = self.__contour.get_contours()
        self.__contour.set_contours([c for c in contours if min_area < cv2.contourArea(c) < max_area])
        return self

    def filter_by_perimeter(self, min_perimeter: int = 0, max_perimeter: int = 1000):
        contours = self.__contour.get_contours()
        self.__contour.set_contours([c for c in contours if min_perimeter < cv2.arcLength(c, True) < max_perimeter])
        return self

    def filter_by_sides(self, min_sides: int = 0, max_sides: int = 1000):
        contours = self.__contour.get_contours()
        self.__contour.set_contours(
            [c for c in contours if min_sides < len(cv2.approxPolyDP(c, 0.02*cv2.arcLength(c,True), True))]
        )
        return self


class Draw:
    def __init__(self, image: Image, contour: Contour, color: tuple = (0, 255, 0)):
        self.__image = image
        self.__color = color
        self.__contour = contour

    def set_color(self, color: tuple):
        self.__color = color
        return self

    def image_contour(self):
        img = image.get()
        cv2.drawContours(img, contour.get_contours(), -1, self.__color, 1)
        image.set(img)
        return self

    def image_rectangle(self):
        img = image.get()
        for c in contour.get_contours():
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), self.__color, 2)
        image.set(img)
        return self

    def original_contour(self):
        img = image.get_original()
        cv2.drawContours(img, contour.get_contours(), -1, self.__color, 1)
        image.set(img)
        return self

    def original_rectangle(self):
        img = image.get_original()
        for c in contour.get_contours():
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), self.__color, 2)
        image.set(img)
        return self

    def contour(self, select: str = "image"):
        if select == "image":
            return self.image_contour()
        elif select == "original":
            return self.original_contour()
        return self

    def rectangle(self, select: str = "image"):
        if select == "image":
            return self.image_rectangle()
        elif select == "original":
            return self.original_rectangle()
        return self


class Coordinates:
    def __init__(self, contour: Contour):
        self.__contour = contour
        self.__coordinates = None

    def set(self, coordinates: list):
        self.__coordinates = coordinates
        return self

    def get(self):
        return self.__coordinates

    def process(self, c: int):
        self.__coordinates = [(cv2.boundingRect(c), c) for c in self.__contour.get_contours()]
        return self.__coordinates


if __name__ == '__main__':
    image = Image()
    image.read_path(r"C:\Users\bekta\PycharmProjects\OOB\assets\images\4.jpg")
    color = Color(image)
    thresh = Thresh(image)
    contour = Contour(image)
    draw = Draw(image, contour)
    filter = Filter(contour)
    coordinate = Coordinates(contour)

    color.to_gray()
    thresh.threshold(96)
    contour.find()
    image.show().wait_key(0)
    filter.filter_by_area(15, 25000)
    # print("contours: ", contour.get_contours())
    coordinate.process(10)
    draw.contour("original")
    # draw.rectangle("original")
    image.show("Contours").wait_key(0)
    print("Coordinates: ", coordinate.get())

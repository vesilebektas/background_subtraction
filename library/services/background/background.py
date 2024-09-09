from library.objects.image.image import Image
from library.objects.color.color import Color
from library.objects.threshold.threshold import Thresh
import numpy as np


class BackgroundSub:
    def __init__(self, image: Image):
        self.__image = image
        self.__white_dots = None
        self.__black_dots = None
        self.__white_coordinates = None
        self.__black_coordinates = None

    def count_white_dots(self):
        self.__white_dots = np.count_nonzero(self.__image.get() == 255)
        return self.__white_dots
    # np.count_nonzero() fonksiyonu kullanılarak görüntüdeki piksel değerlerinin 255'e eşit olanları sayılır

    def count_black_dots(self):
        self.__black_dots = np.count_nonzero(self.__image.get() == 0)
        return self.__black_dots

    def white_coordinates(self):
        self.__white_coordinates = np.argwhere(self.__image.get() == 255)
        return self.__white_coordinates
    # np.argwhere() görüntüdeki piksel değerlerinin 255'e eşit olanların koordinatları bulunur
    # self.__image.get() == 255 beyaz piksellerin bulunmasını sağlar

    def black_coordinates(self):
        self.__black_coordinates = np.argwhere(self.__image.get() == 0)
        return self.__black_coordinates

    def process_coordinates(self, coordinates):
        image = self.__image.get_original()
        for coordinate in coordinates:
            image[coordinate[0], coordinate[1]] = 0
        self.__image.set(image)
    # Bu fonksiyonun amacı belirli koordinatlardaki piksellerin değerlerini değiştirmektir.
    # coordinate değerleri alınır ve 0'a eşitlenir yani siyah yapılır.

    def process(self):
        if self.count_black_dots() > self.count_white_dots():
            coordinates = self.black_coordinates()
        else:
            coordinates = self.white_coordinates()

        self.process_coordinates(coordinates)
        return self


if __name__ == "__main__":
    image = Image().read_path(r'C:\Users\bekta\PycharmProjects\OOB\assets\images\4.jpg')

    color = Color(image)
    color.to_gray()

    thresh = Thresh(image)
    thresh.threshold(th_min=127, th_max=255)

    background = BackgroundSub(image)
    background.process()

    image.show('Kumas')
    image.show("original")
    image.wait_key(delay=0)

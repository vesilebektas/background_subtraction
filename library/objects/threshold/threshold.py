from library.objects.image.image import Image
from library.objects.color.color import Color
import cv2


class Thresh:
    def __init__(self, image: Image):
        self.__image = image

    # def threshold(self, th_min: float = 100, th_max: float = 255):
    #     ret, img = cv2.threshold(self.__image.get(), th_min, th_max, cv2.THRESH_BINARY_INV)
    #     self.__image.set(img)
    #     return self

    def threshold(self, th_min: float = 127, th_max: float = 255):
        img = cv2.threshold(self.__image.get(), th_min, th_max, cv2.THRESH_BINARY_INV)[1]
        self.__image.set(img)
        return self

    def binary(self, th_min: float = 100, th_max: float = 255):
        ret, img = cv2.threshold(self.__image.get(), th_min, th_max, cv2.THRESH_BINARY)
        self.__image.set(img)
        return self

    def adaptive(self, block_size: int, c: int):
        self.__image.set(
            cv2.adaptiveThreshold(
                self.__image.get(),
                255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,
                block_size,
                c
            )
        )
        return self

    def otsu(self, th_min: float = 0, th_max: float = 255):
        ret, img = cv2.threshold(self.__image.get(), th_min, th_max, cv2.THRESH_OTSU)
        return self


if __name__ == '__main__':
    image = Image().read_path(r"C:\Users\bekta\PycharmProjects\OOB\assets\images\6.jpg")
    color = Color(image)
    thresh = Thresh(image)

    color.to_gray()

    image.show("Gray").wait_key(0)

    thresh.threshold()
    image.show("Threshold").wait_key(0)

    image.show("original").wait_key(0)

    # thresh.binary()
    # image.show("Binary").wait_key(0)
    #
    # thresh.adaptive(11, 4)
    # image.show("Adaptive").wait_key(0)
    #
    # thresh.otsu()
    # image.show("Otsu").wait_key(0)

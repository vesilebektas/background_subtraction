from library.objects.image.image import Image
from library.objects.color.color import Color
import cv2


class Canny:
    def __init__(self, image: Image):
        self.__image = image

    def canny(self, min_threshold: int, max_threshold: int):
        self.__image.set(cv2.Canny(self.__image.get(), min_threshold, max_threshold))
        return self


if __name__ == '__main__':
    image = Image()
    image.read_path(r"C:\Users\bekta\PycharmProjects\OOB\assets\images\4.jpg")
    image.show("Original").wait_key(0)
    color = Color(image)
    color.to_gray()

    image.show("Original Gray").wait_key(0)
    canny_detector = Canny(image)
    canny_detector.canny(85, 150)
    image.show("**").wait_key(0)

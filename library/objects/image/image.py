import cv2
from copy import deepcopy


class Image:
    def __init__(self, image_path: str = None):
        self.__image = None
        self._image_path = image_path
        self.__width = None
        self.__height = None
        self.__channels = None
        self.__original = None

    def read_path(self, image_path: str):
        self._image_path = image_path
        self.__image = cv2.imread(image_path)
        if self.__original is None:
            print("Set original")
            self.set_original(self.__image)
        else:
            print("Original is.")
        self.shape()
        return self

    def set(self, image: cv2.Mat):
        self.__image = deepcopy(image)
        if self.__original is None:
            print("Set original")
            self.set_original(self.__image)
        else:
            print("Original Is.")
        return self

    def set_original(self, img: cv2.Mat):
        print("Set Original")
        self.__original = deepcopy(img)
        return self

    def shape(self):
        if len(self.__image.shape) == 2:
            self.__channels = 1
        else:
            self.__height, self.__width, self.__channels = self.__image.shape
        return self

    def get(self):
        return self.__image

    def get_original(self):
        return deepcopy(self.__original)

    def get_path(self):
        return self._image_path

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_channels(self):
        return self.__channels

    def show(self, title: str = "Image"):
        if title == "original":
            cv2.imshow(title, self.__original)
        else:
            cv2.imshow(title, self.__image)
        return self

    def wait_key(self, delay: int = 0, key: int = ord('q')):
        if cv2.waitKey(delay) == key:
            return key


if __name__ == '__main__':
    image = Image()
    image.read_path(r"C:\Users\bekta\PycharmProjects\OOB\assets\images\6.jpg")
    image.show("Kumas").wait_key(delay=0)
    print("Image Width", image.get_width())
    print("Image Height: ", image.get_height())
    print("Image Channels: ", image.get_channels())

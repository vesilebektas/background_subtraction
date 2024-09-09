from library.objects.image.image import Image
import cv2


class Color:
    def __init__(self, img: Image):
        self.__image = img

    def to_gray(self):
        self.__image.set(
            cv2.cvtColor(
                self.__image.get(),
                cv2.COLOR_BGR2GRAY
            )
        )
        return self

    def to_hsv(self):
        img = self.__image.get()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        self.__image.set(hsv)
        return self

    def to_rgb(self):
        img = self.__image.get()
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.__image.set(rgb)
        return self

    def to_hls(self):
        img = self.__image.get()
        hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        self.__image.set(hls)
        return self


if __name__ == '__main__':
    image = Image()
    image.read_path(r"C:\Users\bekta\PycharmProjects\OOB\assets\images\6.jpg")
    color = Color(image)
    image.show("Kumas")
    color.to_gray()
    image.show("Kumas")

    print("Image Width: ", image.get_width())
    print("Image Height: ", image.get_height())
    print("Image Channels: ", image.get_channels())

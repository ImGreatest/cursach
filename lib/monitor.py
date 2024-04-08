import pyautogui as pag
from pyautogui import Size, Point


class Monitor:
    """
    Class for interact with hardware devices and getting useful information.
    """
    def __init__(self):
        self._size = pag.size()
        self._position = pag.position()

    def __repr__(self):
        return "{}, {}".format(self._size, self._position)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_value):
        self._size = new_value

    @size.deleter
    def size(self):
        del self._size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_value):
        self._position = new_value

    @position.deleter
    def position(self):
        del self._position

    @staticmethod
    def get_on_screen_value(x: int, y: int) -> bool:
        """
        Define visible app on the screen
        :param x: position on x-line
        :param y: position on y-line
        :return: True if x & y are within tre screen
        """
        return pag.onScreen(x, y)

    def get_monitor_size(self) -> Size:
        """
        :return: Current screen resolution width and height
        """
        return self._size

    def get_mouse_position(self) -> Point:
        """
        :return:current mouse x and y on the screen
        """
        return self._position

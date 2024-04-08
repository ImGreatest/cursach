from abc import ABC, abstractmethod


class Service(ABC):

    @abstractmethod
    def open_connection(self):
        pass

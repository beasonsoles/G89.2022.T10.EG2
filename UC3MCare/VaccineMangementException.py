"""
Module that comprises any exceptions that might be raised in VaccineManager
"""


class VaccineManagementException(Exception):
    """
    Class that creates a message when there is an exception
    """
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

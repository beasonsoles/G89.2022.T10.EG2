"""
Module that manages requests of vaccines by the clients
"""
import json
from datetime import datetime

class VaccineRequest:
    """
    Class that contains properties and setters for both
    the phone and id document of a client and returns
    """
    def __init__(self, idcode, phoneNumber):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def Phone(self):
        return self.__phoneNumber
    @Phone.setter
    def Phone(self, value):
        self.__phoneNumber = value

    @property
    def idDocument(self):
        return self.__idcode
    @idDocument.setter
    def idDocument(self, value):
        self.__idcode = value

    @property
    def time_stamp(self):
        return self.__time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self.__time_stamp = value

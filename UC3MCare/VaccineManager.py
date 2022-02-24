"""
Module that manages the vaccines to be administered to different clients
"""
import json
import re
import uuid

from UC3MCare.VaccineMangementException import VaccineManagementException
from UC3MCare.VaccineRequest import VaccineRequest


class VaccineManager:
    """
    class that includes the methods ValidateGUID and ReadaccessrequestfromJSON
    """
    def Init(self):
        pass

    @staticmethod
    def ValidateGUID(guid):
        """
        Method that receives a GUID and raises an error if it is invalid
        """
        try:
            uuid.UUID(guid)
            myregex = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-'
                                 r'[89AB][0-9A-F]{3}-[0-9A-F]{12}$',
                                 re.IGNORECASE)
            x = myregex.fullmatch(guid)
            if not x:
                raise VaccineManagementException("Invalid UUID v4 format")
        except ValueError as e:
            raise VaccineManagementException("Id received is not a UUID") from e
        return True

    def ReadaccessrequestfromJSON(self, fi):
        """
        Method that raises an error if the entered file is incorrect
        or if the JSON format is wrong
        """
        try:
            with open(fi, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise VaccineManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VaccineManagementException("JSON Decode Error - "
                                             "Wrong JSON Format") from e
        try:
            Guid = data["id"]
            Zip = data["phoneNumber"]
            req = VaccineRequest(Guid, Zip)
        except KeyError as e:
            raise VaccineManagementException("JSON Decode Error - "
                                             "Invalid JSON Key") from e
        if not self.ValidateGUID(Guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return req

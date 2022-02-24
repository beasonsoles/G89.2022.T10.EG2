"""
Module that encodes and decodes a request
"""

import string
from UC3MCare import VaccineManager


# GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def Encode(word):
    """
    Function that encodes an entered word
    """
    encoded = ""
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Decode(word):
    """
    Function that decodes an entered word
    """
    encoded = ""
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Main():
    """
    Function that prints a request and its encoding and decoding
    """
    mng = VaccineManager()
    res = mng.ReadaccessrequestfromJSON("test.json")
    strRes = res.__str__()
    print(strRes)
    EncodeRes = Encode(strRes)
    print("Encoded Res " + EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)


if __name__ == "__main__":
    Main()

from typing import Any
"""
מגישים:
מתן זיסמן - 316217983
קירה אפרמוב 337640387
"""
class infoUnit:

    """
        This class represents InfoUnit.
        Info units will be used to store information in LRUcaches.

    """

    def __init__(self, key: str = "", value: [int, Any] = 0):
        """
        Constructur of an infoUnit Node, that will contain a pair of key and value.
        :param key: a key that represents this infoUnit uniqeness, could also be uniqe information.
        :param value: Information stored by the unit, can be logically determined by the stored key.
        """

        self.key = key
        self.value = value
        self.next = None
        self.prev = None


    def getKey(self) -> Any:
        """
        Function that retrieves the key of the infoUnit.
        :return: returns the infoUnit's uniqe key.
        """
        return self.key


    def getValue(self) -> Any:
        """
        Function that retrieves the value of the infoUnit.
        :return: returns the information stored as value by the unit.
        """
        return self.value


    def setKey(self, key: str) -> None:
        """
        Assigns a new key to a chosen infoUnit.
        :param key: The new key that will replace the current one.
        :return: Doing a background operation, returns None.
        """
        self.key = key


    def setValue(self, value: [int, Any] = 0 ) -> None:
        """
        Assigns a new value to a chosen infoUnit.
        :param value: The new value that will replace the current one.
        :return: Doing a background operation, returns None.
        """
        self.value = value


    def __str__(self) -> str:
        """
        Function that replaces the default __str__ function from Object.
        :return: a string that will replace the default string that is usually returned by print().
        """
        str = f"Node key: {self.key}, Node value: {self.value}\n"
        return str
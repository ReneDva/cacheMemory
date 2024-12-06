from typing import Any
from info_unit import infoUnit


class LRUcache:
    def __init__(self, size: int):
        """
        Defines a new LRUcache structure that can be use to store uniqe keys(information) paired with values(matching information according to logic of code)
        :param size: Defines the infoUnits capacity of the LRUcache, as each pair of key and value is one infoUnit.
        """
        self._capacity = size
        self._head = infoUnit(None, None)
        self._tail = infoUnit(None, None)
        self._cache = {}
        self._head.next = self._tail
        self._tail.next = self._head

    def _moveToFirst(self, infoUnit) -> None:
        """
        Recieves infoUnit and moves it to be the first infoUnit in a sentinel doubly linked list.
        :param infoUnit: The unit that needs to be moved.
        :return: Background operation, returns None.
        """
        pointer = infoUnit
        pointer.next.prev = pointer.prev
        pointer.prev.next = pointer.next
        pointer.next = self._head.next
        pointer.prev = self._head
        self._head.next.prev = pointer
        self._head.next = pointer


    def put(self, key: str = '',value: [int, Any] = 0) -> None:
        """
        Inserts new infoUnit to the LRUcache structures, followed by last recently used logic.
        :param key: The key of the new infoUnit.
        :param value: The value of the new infoUnit.
        :return: Background operation, returns None.
        """
        Node = infoUnit(key = key, value = value)

        if (key in self._cache):      #if identical key is in memory
            pointer = self._cache[key]
            pointer.setValue(value)
            self._moveToFirst(pointer)

        else:                        #any other case.
            if (len(self._cache) >= self._capacity):
                if (self._sizeIsZero()):                #if memory infoUnits capacity is 0.
                    print('Cache cannot memorise data - Capacity is 0')
                    return
                pointer = self._tail.prev               #capacity is not 0, but list is full
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                del self._cache[pointer.getKey()]

            pointer = Node                             #add the new infoUnit to head of sentinel list.
            self._head.next.prev = pointer
            pointer.next = self._head.next
            self._head.next = pointer
            pointer.prev = self._head
            self._cache[key] = pointer
            return


    def get(self, key: Any) -> Any:
        """
        Uses a uniqe key to retriev the paired value, under LRU logic.
        :param key: The chosen uniqe key.
        :return: If the uniqe key is in the LRU Structure, it will return the paired value. Else - None.
        """
        if (key in self._cache):           #if identical key is in memory.
            pointer = self._cache[key]
            self._moveToFirst(pointer)    #moves reached infoUnit to head of the sentinel list.
            return pointer.getValue()     #returns valeu of reached unit
        else:
            return None                   #if not - return none.


    def _sizeIsZero(self) -> bool:
        """
        Tests if the capacity equals 0 to avoid Running-Errors.
        :return: True/False according to capacity value.
        """
        return (self._capacity == 0)


    def _readLast(self) -> None:
        """
        Additional function: Used to read the last recently used infoUnit.
        :return: String that will present the last recently used infoUnit key and value.
        """
        if (self._tail.prev != self._head):    #if the list is not empty.
          str = f"{self._tail.prev.getKey()}: {self._tail.prev.getValue()}"
          print(str)
        return


    def __str__(self) -> str:
        """
        Function that replaces the default __str__ function from Object.
        :return: a string that will replace the default string that is usually returned by print().
        """
        result =''
        pointer = self._head.next
        while pointer and pointer!= self._tail:                       #loop over each infoUnit.
            result += (f"{pointer.getKey()} :{pointer.getValue()}\n") #connect its values to a string by format
            pointer = pointer.next
        return result





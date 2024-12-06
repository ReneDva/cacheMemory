import pandas as pd
from lru_cache import LRUcache
from Calculation import Calculation

class CacheCalculator(LRUcache):
    def __init__(self, size: int):
        """
        Defines CacheCalculator, a Calculator that uses LRU logic and can store previous values.
        :param size: capacity for amount of previous calculations that can be stored.
        """
        super().__init__(size)
        self.operator_mapping = {'sum': '+', 'sub': '-', 'div': '/', 'mul': '*'}

    def strToChar(self, operator=str) -> str:
        """
        Translates user chosen operators to actual operator.
        :param operator: User operator.
        :return: Actual operator, example: User chose 'sum' -> returns '+'.
        """
        if (operator in self.operator_mapping):
            return self.operator_mapping[operator]  # Convert given known operator to arithmethic operator.
        else:
            raise ValueError('Unkown operator. Known operators: sum, sub, div, mul.')


    def calculate(self, left_side = [int, float], right_side = [int, float], operator = str) -> tuple:
        """
        Recieves arithmethic expression,
        While operator is known (monitored by 'Calculation' Class), It will use 'Calculation' class to calculate the result.
        It will than retrieve the expression as key and result as value to manage the memory LRU-logicwised.
        :param left_side: the left number of the arithmetic expression.
        :param right_side: the right number of the arithmetic expression.
        :param operator: the operator of the arithmetic expression.
        :return: Tuple with 2 slots, One for the result of the calculaiton and the other for boolean flag that will
                 declare True if the result came from the LRU structure memory or false if it had to be calculated.
        """
        calculation = Calculation(left_side, right_side, self.strToChar(operator))
        key = calculation.getKey()
        if (self.get(key = key) == None):
            result = calculation.getValue()
            self.put(key = key, value = result)
            return (result, False)
        else:
            result = self.get(key)
            return (result, True)


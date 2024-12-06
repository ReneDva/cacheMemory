from typing import Any
from info_unit import infoUnit

class Calculation(infoUnit):

    def __init__(self, left_side = [int, float], right_side = [int, float] ,operator = str):
        """
        Defines a new Calculation structure, uses 3 parameters to define which calculation and than connects them
        to a string for key and an int for value.
        :param left_side: A number that will be located on the left side of the calculation.
        :param right_side:  A number that will be located on the right side of the calculation.
        :param operator: The operator, possible operations defined in operator_mapping.
        """
        key = f"{left_side}{operator}{right_side}"
        result = eval(f"{left_side}{operator}{right_side}")   #result of specifiec calculation.
        super().__init__(key = key, value = result)



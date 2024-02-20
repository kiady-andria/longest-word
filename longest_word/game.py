# pylint: disable=too-few-public-methods
"""This module contains the Game class used to play the longtest game"""

import random
import string


class Game:
    """Represents the longest word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        string_list = string.ascii_uppercase
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string_list))




    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if len(word) == 0 :
            return False

        return all((letter in self.grid for letter in word ))

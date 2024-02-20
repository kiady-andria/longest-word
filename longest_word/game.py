# pylint: disable=too-few-public-methods
"""This module contains the Game class used to play the longtest game"""

import random
import string
import requests

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
        url = 'https://wagon-dictionary.herokuapp.com/'
        r = requests.get(url + word).json()

        if len(word) == 0 : #Exclude "" as a valid answer
            return False

        if all((letter in self.grid for letter in word )) : #checks if all character in words are in the grid
            if r.get("found") : #Checks if the word is in the dictionnary API
                return True

        return False

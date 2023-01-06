# ThreeCardPoker.py
# by Ballerina Liang
# April 26, 2022
# A game of Three Card Poker where the player plays against the dealer (computer)

import random
import time


class Card:
    # A class of cards in a standard deck with different suits and values
    suits = [chr(9829), chr(9830), chr(9827), chr(9824)]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    valuesnum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # includes integer value for face cards

    # initialize attributes of a card
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # converts the values from a string to integer values for sorting and comparing
    def get_value(self):
        num = self.valuesnum[self.values.index(self.value)]
        return num

    # Return suit attribute of a card
    def get_suit(self):
        return self.suit

    # Returns a string representation of the card itself
    def __repr__(self):
        return f"{self.value} of {self.suit}"

    # Magic methods allowing comparison for sort() function
    def __lt__(self, other):  # checks if current card's value is less than other
        num = self.values.index(self.value)
        num2 = self.values.index(other.value)
        return num < num2

    def __gt__(self, other):  # checks if current card's value is greater than other
        num = self.values.index(self.value)
        num2 = self.values.index(other.value)
        return num > num2

    def __eq__(self, other):  # checks if current card's value is equal to other
        num = self.values.index(self.value)
        num2 = self.values.index(other.value)
        return num == num2


class Deck:
    # A class/deck of cards that knows how to shuffle and deal
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]

    # shuffles deck of cards randomly
    def shuffle(self):
        random.shuffle(self.cards)

    # removes top card from deck and deals one at a time (to dealerhand or playerhand)
    def dealCard(self):
        takeCard = self.cards.pop(0)
        return takeCard
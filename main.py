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


def HighCard(player, dealer):
    """Compares the player and dealer's highest card.
    Parameters
      player(list): list of player's three cards
      dealer(list): list of dealer's three cards
    Return
      0: if player and dealer have the same highest card
      1: if dealer has higher highest card
      2: if dealer has higher highest card
    """
    if player[0].get_value() == dealer[0].get_value():
        return 0
    elif player[0].get_value() < dealer[0].get_value():
        return 1
    else:
        return 2


def Pair(hand):
    """Checks if hand of cards has any pairs.
    Parameters
      hand(list): list of three card objects (either player or dealer's hand)
    Return
      True: if a pair is found
      False: if a pair is not found
    """
    if hand[0].get_value() == hand[1].get_value():
        return True
    elif hand[0].get_value() == hand[2].get_value():
        return True
    elif hand[1].get_value() == hand[2].get_value():
        return True
    '''else:
      return False'''


def Flush(hand):
    """Checks if hand of cards has a Flush.
    Parameters
      hand(list): list of three card objects
    Return
      True: if a Flush is found
    """
    for i in range(1, 3):
        if hand[0].get_suit() is not hand[i].get_suit():
            return False
    return True


def Straight(hand):
    """Checks if hand of cards has a Straight.
    Parameters
      hand(list): list of three card objects
    Return
      True: if a Straight is found
    """
    for i in range(2):
        if hand[i].get_value() != 1 + hand[i + 1].get_value():
            return False
    return True


def ThreeOfaKind(hand):
    """Checks if hand of cards has Three of a Kind.
    Parameters
      hand(list): list of three card objects
    Return
      True: if a Three of a Kind is found
    """
    for i in range(1, 3):
        if hand[0].get_value() != hand[i].get_value():
            return False
    return True


def StraightFlush(hand):
    """Checks if hand of cards has a Straight Flush.
    If both a Straight and Flush is found in a hand (both return true), it must also contain a Straight Flush.
    Parameters
      hand(list): list of three card objects
    Return
      True: if a Straight Flush is found
    """
    return Straight(hand) and Flush(hand)


def HandType(rank):
    """Returns the "hand" type as a string according to the rank.
    Parameters
      rank(int): rank of a person's hand of cards
    Return
      The "hand" type as a string
    """
    if rank == 1:
        return "Straight Flush"
    elif rank == 2:
        return "Three of a Kind"
    elif rank == 3:
        return "Straight"
    elif rank == 4:
        return "Flush"
    elif rank == 5:
        return "Pair"
    elif rank == 6:
        return "High Card"


# ---------Game--------
again = ""
while True:
    if again == "N":
        break  # Game ends and compiler stops running.
    elif again == "Y":
        print("reshuffling...\n")
        time.sleep(1)

    print("Hello!")
    money = 500  # player's starting balance (resets after 6 games)

    d = Deck()  # create a deck of cards
    d.shuffle()  # shuffle deck of cards

    player = []  # list of playerhand lists (After 6 games in a row, player list will have 6 playerhand lists)
    dealer = []  # list of dealerhand lists

    for i in range(6):  # allows player to play 6 games in a row before reshuffling

        print(f"Welcome to a game of Three-Card Poker. You have a balance of ${money}. How much would you like to bet?")

        # asks user for betting amount and error handles
        try:
            bet = int(input("> $"))
        except:
            print("You must enter an integer.")
            continue
        else:
            if bet < 1 or bet > money:
                print(f"Your choice must be an integer between 1 to {money}.")
                continue
        money = money - bet  # take bet amount from player's balance

        playerhand = []  # a list of player's three cards each game
        dealerhand = []  # a list of dealer's three cards each game
        for count in range(3):
            # deals 3 cards to playerhand and dealerhand
            playerhand.append(d.dealCard())
            dealerhand.append(d.dealCard())
        player.append(playerhand)  # store list of three cards from each game
        dealer.append(dealerhand)
        # sort player and dealer's list of 3 cards from highest to lowest using sort() function
        player[i].sort(reverse=True, key=Card.get_value)
        dealer[i].sort(reverse=True, key=Card.get_value)

        # display player's three cards
        print("Your cards:", player[i])
        print(" ___   ___   ___ ")
        print(f"|{player[i][0].value}  | |{player[i][1].value}  | |{player[i][2].value}  |")
        print(f"| {player[i][0].suit} | | {player[i][1].suit} | | {player[i][2].suit} |")
        print(f"|__{player[i][0].value}| |__{player[i][1].value}| |__{player[i][2].value}|")

        #
        try:
            play = int(input("\nDo you wish to 1) Double your bet or 2) Fold your hand (give up)? "))
        except:
            print("You must enter an int.")
            continue
        else:
            if play < 1 or play > 2:
                print("You must enter 1 or 2.")
                continue
            elif play == 2:
                again = "Y"
                print("\nDealer wins.")
                break

        ranks = [7, 7]  # ranks[0] = player rank, ranks[1] = dealer's rank
        hands = [player[i], dealer[i]]  # contains player and dealer's list of three cards
        # 1 -> highest rank (straight flush), 7 -> lowest rank
        # Determine player and dealer's rank
        for k in range(2):
            if StraightFlush(hands[k]):
                ranks[k] = 1
            elif ThreeOfaKind(hands[k]):
                ranks[k] = 2
            elif Straight(hands[k]):
                ranks[k] = 3
            elif Flush(hands[k]):
                ranks[k] = 4
            elif Pair(hands[k]):
                ranks[k] = 5

        # Determine the winner or if it is a tie according to their ranks
        winner = ""
        if ranks[0] < ranks[1]:
            winner = "Player"
        elif ranks[0] > ranks[1]:
            winner = "Dealer"
        elif ranks[0] == 5 and ranks[1] == 5:
            # if player and dealer both have a pair
            playerpairvalue = 0
            dealerpairvalue = 0
            for x in range(3):  # find pair value in player hand
                for y in range(x + 1, 3):
                    if player[i][x].get_value() == player[i][y].get_value():
                        playerpairvalue = player[i][x].get_value()
            for x in range(3):  # find pair value in dealer hand
                for y in range(x + 1, 3):
                    if dealer[i][x].get_value() == dealer[i][y].get_value():
                        dealerpairvalue = dealer[i][x].get_value()
            if playerpairvalue > dealerpairvalue:
                winner = "Player"
            elif playerpairvalue < dealerpairvalue:
                winner = "Dealer"
            else:
                winner = "Tie"
        else:  # if player and dealer have the same rank excluding rank 5 (a pair), compare highest card
            if HighCard(player[i], dealer[i]) == 2:  # player has high card
                if ranks[0] == 7:
                    ranks[0] = 6  # person with high card is assigned rank 6
                winner = "Player"
            elif HighCard(player[i], dealer[i]) == 1:  # dealer has high card
                if ranks[1] == 7:
                    ranks[1] = 6
                winner = "Dealer"
            elif HighCard(player[i], dealer[i]) == 0:
                ranks[0] = 6
                ranks[1] = 6
                winner = "Tie"

        # Display Dealer's cards
        print("\nRevealing Dealer's 3 cards...")
        time.sleep(1.5)
        print("Dealer's cards:", dealer[i])
        print(" ___   ___   ___ ")
        print(f"|{dealer[i][0].value}  | |{dealer[i][1].value}  | |{dealer[i][2].value}  |")
        print(f"| {dealer[i][0].suit} | | {dealer[i][1].suit} | | {dealer[i][2].suit} |")
        print(f"|__{dealer[i][0].value}| |__{dealer[i][1].value}| |__{dealer[i][2].value}|")
        time.sleep(1.5)

        # Payout system and winner message
        payout = 0
        playerHandType = HandType(ranks[0])
        dealerHandType = HandType(ranks[1])
        if winner == "Player":
            # Determine payout amount according to player's rank/hand
            if ranks[0] == 1:
                payout = bet * 20
            elif ranks[0] == 2:
                payout = bet * 10
            elif ranks[0] == 3:
                payout = bet * 6
            elif ranks[0] == 4:
                payout = bet * 3
            elif ranks[0] == 5:
                payout = bet * 2
            elif ranks[0] == 6:
                payout = bet
            print(f"You win ${payout} with a better Hand of {playerHandType}!")
        elif winner == "Dealer":
            print(f"The Dealer wins with a better Hand of {dealerHandType}.\nYou lost your bet amount of ${bet}.")
        elif winner == "Tie":
            if ranks[0] == 1:
                payout = bet * 20 / 2  # player only gets half of original payout if a tie
            elif ranks[0] == 2:
                payout = bet * 10 / 2
            elif ranks[0] == 3:
                payout = bet * 6 / 2
            elif ranks[0] == 4:
                payout = bet * 3 / 2
            elif ranks[0] == 5:
                payout = bet * 2 / 2
            elif ranks[0] == 6:
                payout = bet / 2
            print(
                f"You and the Dealer both tie with a Hand of {playerHandType}! Half of your bet amount ${bet / 2} is returned.")
        money = money + payout  # add payout to player balance

        print()
        # Ask if user would like to play again.
        while True:
            again = input("Would you like to play again? [Y]es or [N]o: ")
            again = again.upper()  # makes player's choice upper case
            print()
            if again == "Y" or again == "N":
                break
            else:
                print("Your choice must be either \"Y\" or \"N\".")
                continue

        # If player runs out of money or chooses not to play again, break out of loop and return to beginning of while loop
        if money < 1:
            again = "N"
            print("Sorry, you have insufficient funds to play another game.")
            break
        elif again == "N":
            print("Thank you for playing!")
            break
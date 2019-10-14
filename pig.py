# IS211_Assignment7 Pig Game

import random


class Dice(object):
    random.seed(0)

    def __init__(self):
        self.rolled = 0

    def roll(self):
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):

    def __init__(self, name):
        self.name = name
        self.score_total = 0
        self.score_turn = 0
        self.turn_num = 0
        print('Please Start the game {}'.format(self.name))


def raw_input():
    pass


class Game(object):

    """ Example
print(Game('X', 'Y'))


Please Start the game X
Please Start the game Y
Player turn: X
X rolled a 4
X has a current score of 4.with a total score of 4
X, Roll (R/r) the dice?  or Hold (H/h) this turn? r
Player turn: X
X rolled a 4
X has a current score of 4.with a total score of 8
X, Roll (R/r) the dice?  or Hold (H/h) this turn? h
X stands with a total score of 12
X score is 12. Next player roll the dice please!!
Player turn: Y
Y rolled 1, lost your turn.
Y, your current score is 0
Player turn: X
X rolled a 3
X has a current score of 3.with a total score of 15
X, Roll (R/r) the dice?  or Hold (H/h) this turn? """
    def __init__(self, player1, player2):

        """ Args:
            player1 (string) : the name of player 1.
            player2 (string): the name of player 2.

        Attributes:
            Game (class): invokes the game class.
            Player (class): Invokes the player class.
            player1 (string) : the name of player 1.
            player2 (string): the name of player 2.

        """

        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.dice = Dice()
        self.turn(self.player1)

    def turn(self, player):

        player.turn_num = 1
        print('Player turn: {}'.format(player.name))
        if player.turn_num == 1 and player.score_total < 100:
            roll = self.dice.roll()
            if roll == 1:
                print('{} rolled 1, lost your turn.'.format(player.name))
                print('{}, your current score is {}'.format(player.name, player.score_total))
                player.score_turn = 0
                self.next_player()
            else:
                print("{} rolled a {}".format(player.name, roll))
                player.score_turn = roll
                player.score_total += player.score_turn
                print(
                    ("{} has a current score of {}." "with a total score of {}").format(player.name, player.score_turn,
                                                                                        player.score_total))
                self.turn_select(player)

        else:
            player.score_total >= 100
            print(('You Won!! '"{} wins the game!" "with a total score of {}").format(player.name, player.score_total))

    def turn_select(self, player):
        """Args:
            player (string) The name of the player.
        Returns:
            String (string): A meesage to display the player's name, current score, and total score."""

        select = input('{}, Roll (R/r) the dice? ' " or Hold (H/h) this turn? ".format(player.name))
        select = (select[0])
        if select.lower() == 'h':
            player.score_total += player.score_turn
            print(('{} stands with a total score of {}').format(player.name, player.score_total))

            if player.score_total >= 100:
                print('You WON!!!'" {} wins the game!!" ' Total Score Of {} ').format(player.name, player.score_total)

                raise SystemExit
            else:
                player.score_turn = 0
                print(("{} score is {}. " "Next player roll the dice please!!").format(player.name, player.score_total))

                self.next_player()
        elif select.lower() == 'r':
            self.turn(player)
        else:
            print(" Please Enter R/r to Roll or H/h To Hold The Dice. ")
            self.turn_select(player)

    def next_player(self):

        if self.player1.turn_num == 1:
            self.player1.turn_num = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)


#print(Game('X', 'Y'))

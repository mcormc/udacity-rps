#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        self.move_temp = "rock"

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.move_temp = "rock"

    def move(self):
        if self.move_temp == "rock":
            return "paper"
        elif self.move_temp == "paper":
            return "scissors"
        elif self.move_temp == "scissors":
            return "rock"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.move_temp = my_move


class HumanPlayer(Player):

    def move(self):
        # iterate for infinite times
        while True:
            # https://wiki.python.org/moin/WhileLoop
            string = input("rock, paper, scissors? ")
            if string.lower() not in moves:
                print("Please choose rock, paper or scissors.")
            else:
                break
        return string

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.win = 0
        self.loss = 0
        self.tie = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1} Player 2: {move2}")
        if beats(move1, move2):
            self.win += 1
        elif beats(move2, move1):
            self.loss += 1
        else:
            self.tie += 1
        print(f"Score - P1: {self.win} P2: {self.loss} Tie: {self.tie}\n\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\033[31;1mGAME START!\033[0m\n")
        for round in range(3):
            print(f"\033[32;1;4mRound {round}\033[0m")
            self.play_round()
        if self.win > self.loss:
            print(f"\033[31;1;4mGame over.\033[0m "),
            print(f"Player 1 wins (P1: {self.win} P2: {self.loss})")
        elif self.win < self.loss:
            print(f"\033[31;1;4mGame over.\033[0m "),
            print(f"Player 2 wins (P2: {self.loss} P1: {self.win})")
        else:
            print(f"\033[31;1;4mGame over.\033[0m "),
            print(f"It's a tie. (P1: {self.win} P2: {self.loss})")
        print(f"\n\n\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()

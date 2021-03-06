import numpy as np
import abc
import pygame
import sys
import math
import random
from typing import Type
pygame.init()


class Board(abc.ABC):
    """
    Board class used as parent class for the future playing board

    Parameters
    ___________
    columns : int
        number of Columns
    rows : int
        number of Rows
    size : int
        constant to calculate the size of the play area, stones etc.
    height : int
        height of the display based on rows and size
    width : int
        width of the display based on rows and size
    screen_size : int
        size of the screen based on height and width
    blue : tuple
        color attribute for blue
    black : tuple
        color attribute for black
    red : tuple
        color attribute for red
    yellow : tuple
        color attribute for yellow
    rad : int
        radius of the stones
    screen : function
        pygame function to set the screen up
    font : function
        pygame function to set the font up"""

    def __init__(self):
        self.__columns = 7
        self.__rows = 6
        self.__size = 100

        self.__height = (self.__rows + 1) * self.__size
        self.__width = self.__columns * self.__size
        self.__screen_size = (self.__width, self.__height)

        self.__blue = (0, 0, 255)
        self.__black = (0, 0, 0)
        self.__red = (255, 0, 0)
        self.__yellow = (255, 255, 0)
        self.__rad = int(self.size / 2 - 5)

        pygame.init()
        self.__screen = pygame.display.set_mode(self.__screen_size)
        self.__font = pygame.font.SysFont("arial", 75)

    @property
    def columns(self):
        return self.__columns

    @property
    def rows(self):
        return self.__rows

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def blue(self):
        return self.__blue

    @property
    def black(self):
        return self.__black

    @property
    def red(self):
        return self.__red

    @property
    def yellow(self):
        return self.__yellow

    @property
    def rad(self):
        return self.__rad

    @property
    def screen(self):
        return self.__screen

    @property
    def font(self):
        return self.__font

    # @property
    # def screen_size(self):
    #     return self.__screen_size

    # abstract methods that need to be in the child class
    def make_board(self) -> Type[np.array]:
        """Creates the board

        Returns
        ___________
        numpy array
            a board with no places filled
        """
        pass

    def place_stone(self, board, row, col, stone) -> Type[np.array]:
        """updates the Board with the position of the placed stone

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form
        row : int
            row coordinate where the stone will be placed
        col : int
            col coordinate where the stone will be placed
        stone : int
            identifier for which player placed the stone for ex. 1 for player one
        Returns
        ___________
        board : numpy array
            an updated array of the board with the newly placed stone
        """
        pass

    def loc_valid(self, board, col) -> Type[np.array]:
        """checks if the selected placement is valid

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form
        col : int
            identifier for column position

        Returns
        ___________
        board : numpy array
            an updated board with valid locations
        """
        pass

    def next_row(self, board, col) -> Type[np.array]:
        """checks if the next stone would end up in a new row

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form
        col : int
            identifier for column position

        Returns
        ___________
        board : numpy array
            an updated board
        """
        pass

    def win_cond(self, board, stone) -> bool:
        """win conditions that would result in the end of the game

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form
        stone : int
            identifier for which player placed the stone for ex. 1 for player one

        Returns
        ___________
        bool
            returns True if a win conditions is met
        """
        pass


class PlayBoard(Board):
    def __init__(self):
        super().__init__()

    def make_board(self):
        board = np.zeros((self.rows, self.columns))
        return board

    @staticmethod
    def print_board(board) -> Type[print()]:
        """ prints the numpy array of the board to the console

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form

        Returns
        ___________
        str
            a representation of the array in str format printed to the console
        """
        return print(np.flip(board, 0))

    def place_stone(self, board, row, col, stone):
        board[row][col] = stone
        return board

    def loc_valid(self, board, col):
        return board[self.rows - 1][col] == 0

    def next_row(self, board, col):
        for r in range(self.rows):
            if board[r][col] == 0:
                return r

    def win_cond(self, board, stone):
        # check rows for win condition
        for i in range(self.columns - 3):
            for j in range(self.rows):
                if board[j][i] == stone and board[j][i + 1] == stone and board[j][i + 2] == stone and \
                        board[j][i + 3] == stone:
                    return True

        # check columns for win condition
        for i in range(self.columns):
            for j in range(self.rows - 3):
                if board[j][i] == stone and board[j + 1][i] == stone and board[j + 2][i] == stone and \
                        board[j + 3][i] == stone:
                    return True

        # check pos diagonals for win condition
        for i in range(self.columns - 3):
            for j in range(self.rows - 3):
                if board[j][i] == stone and board[j + 1][i + 1] == stone and board[j + 2][i + 2] == stone and \
                        board[j + 3][i + 3] == stone:
                    return True

        # check neg sloped diagonals for win condition
        for i in range(self.columns - 3):
            for j in range(3, self.rows):
                if board[j][i] == stone and board[j - 1][i + 1] == stone and board[j - 2][i + 2] == stone and \
                        board[j - 3][i + 3] == stone:
                    return True

    @staticmethod
    def draw(board) -> bool:
        """checks if there are still valid places left for stones

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form

        Returns
        ___________
        Bool
            returns True if no more free spaces are available
        """
        if 0 in board:
            pass
        else:
            return True

    # # something isn't working, uncommented in further code
    # def column_full(self, board):
    #     # check if column is full
    #     for i in range(self.columns):
    #         if board[0:1, i:i + 1] == 0:
    #             return False
    #         else:
    #             return True

    def render_board(self, board):
        """renders the board in pygame

        Parameters
        ___________
        board : numpy array
            a representation of the board in array form

        Returns
        ___________
        function
            a pygame display update with the applied settings
        """
        # screen = pygame.display.set_mode(self.screen_size)
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(self.screen, self.blue,
                                 (c * self.size, r * self.size + self.size, self.size, self.size))
                pygame.draw.circle(self.screen, self.black,
                                   (int(c * self.size + self.size / 2), int(r * self.size + self.size + self.size / 2)),
                                   self.rad)

        for c in range(self.columns):
            for r in range(self.rows):
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, self.red, (
                        int(c * self.size + self.size / 2), self.height - int(r * self.size + self.size / 2)), self.rad)
                elif board[r][c] == 2:
                    pygame.draw.circle(self.screen, self.yellow, (
                        int(c * self.size + self.size / 2), self.height - int(r * self.size + self.size / 2)), self.rad)
        pygame.display.update()

    def start_game(self):
        """starts a game of connect 4 and asks the player for multiplayer or single player

        Returns
        ___________
        opens a new window with a game of connect 4 running on it
        """
        multiplayer = input("Multiplayer? Y/N: ")
        multiplayer = multiplayer.upper()
        if multiplayer == 'Y' or multiplayer == 'N':
            multiplayer = multiplayer
        elif multiplayer != 'Y' and multiplayer != 'N':
            multiplayer = 'N'

        play_board = self.make_board()
        game_over = False
        turn = 0

        # pygame.init()
        # screen = pygame.display.set_mode(self.screen_size)
        # font = pygame.font.SysFont("arial", 75)

        self.render_board(play_board)
        pygame.display.update()
        # Ask for Solo or Multiplayer
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.size))
                    position = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(self.screen, self.red, (position, int(self.size / 2)), self.rad)
                    else:
                        pygame.draw.circle(self.screen, self.yellow, (position, int(self.size / 2)), self.rad)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.size))
                    # print(event.pos)
                    # Ask for Player 1 Input
                    if turn == 0:
                        position = event.pos[0]
                        col = int(math.floor(position / self.size))

                        if self.loc_valid(play_board, col):
                            row = self.next_row(play_board, col)
                            self.place_stone(play_board, row, col, 1)

                        if self.draw(play_board):
                            label = self.font.render("Draw!", True, self.blue)
                            self.screen.blit(label, (10, 10))
                            game_over = True

                        if self.win_cond(play_board, 1):
                            label = self.font.render("Player 1 wins!!", True, self.red)
                            self.screen.blit(label, (10, 10))
                            game_over = True

                    # Ask for Player 2 Input
                    else:
                        if multiplayer == 'Y':
                            position = event.pos[0]
                            col = int(math.floor(position / self.size))

                            if self.loc_valid(play_board, col):
                                row = self.next_row(play_board, col)
                                self.place_stone(play_board, row, col, 2)

                            if self.draw(play_board):
                                label = self.font.render("Draw!", True, self.blue)
                                self.screen.blit(label, (10, 10))
                                game_over = True

                            if self.win_cond(play_board, 2):
                                label = self.font.render("Player 2 wins!!", True, self.yellow)
                                self.screen.blit(label, (10, 10))
                                game_over = True

                        elif multiplayer == 'N':
                            col = random.randint(0, 6)

                            if self.loc_valid(play_board, col):
                                row = self.next_row(play_board, col)
                                self.place_stone(play_board, row, col, 2)

                            if self.draw(play_board):
                                label = self.font.render("Draw!!", True, self.blue)
                                self.screen.blit(label, (10, 10))
                                game_over = True

                            if self.win_cond(play_board, 2):
                                label = self.font.render("Player 2 wins!!", True, self.yellow)
                                self.screen.blit(label, (10, 10))
                                game_over = True

                        else:
                            sys.exit()

                    self.print_board(play_board)
                    self.render_board(play_board)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(3000)


if __name__ == '__main__':
    PlayBoard().start_game()

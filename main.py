import numpy as np
import abc
import pygame
import sys
import math


# TODO
# make game end if no one wins, draw function
# make Computer opponent
# Unit Tests
# Doc


class Board(abc.ABC):
    def __init__(self):
        self.__columns = 6
        self.__rows = 7
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
        self.__font = pygame.font.SysFont("monospace", 75)

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

    def make_board(self):
        pass

    def place_stone(self, board, row, col, stone):
        pass

    def loc_valid(self, board, col):
        pass

    def next_row(self, board, col):
        pass

    def win_cond(self, board, stone):
        pass


class PlayBoard(Board):
    def __init__(self):
        super().__init__()

    def make_board(self):
        board = np.zeros((self.rows, self.columns))
        return board

    def print_board(self, board):
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
        # Check horizontal locations for win
        for i in range(self.columns - 3):
            for j in range(self.rows):
                if board[j][i] == stone and board[j][i + 1] == stone and board[j][i + 2] == stone and board[j][
                    i + 3] == stone:
                    return True

        # Check vertical locations for win
        for i in range(self.columns):
            for j in range(self.rows - 3):
                if board[j][i] == stone and board[j + 1][i] == stone and board[j + 2][i] == stone and board[j + 3][
                    i] == stone:
                    return True

        # Check positively sloped diagonals
        for i in range(self.columns - 3):
            for j in range(self.rows - 3):
                if board[j][i] == stone and board[j + 1][i + 1] == stone and board[j + 2][i + 2] == stone and \
                        board[j + 3][i + 3] == stone:
                    return True

        # Check negatively sloped diagonals
        for i in range(self.columns - 3):
            for j in range(3, self.rows):
                if board[j][i] == stone and board[j - 1][i + 1] == stone and board[j - 2][i + 2] == stone and \
                        board[j - 3][i + 3] == stone:
                    return True

        # Check if Spaces are still available
        if 0 in board:
            pass
        else:
            label = self.font.render("Draw!", 1, self.blue)
            return True, label


    def render_board(self, board):
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
        multiplayer = input("Multiplayer? Y/N: ")
        multiplayer = multiplayer.upper()

        playboard = self.make_board()
        game_over = False
        turn = 0

        pygame.init()
        self.render_board(playboard)
        pygame.display.update()
        # Ask for Solo or Multiplayer
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.size))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(self.screen, self.red, (posx, int(self.size / 2)), self.rad)
                    else:
                        pygame.draw.circle(self.screen, self.yellow, (posx, int(self.size / 2)), self.rad)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.size))
                    # print(event.pos)
                    # Ask for Player 1 Input
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.size))

                        if self.loc_valid(playboard, col):
                            row = self.next_row(playboard, col)
                            self.place_stone(playboard, row, col, 1)

                            if self.win_cond(playboard, 1):
                                label = self.font.render("Player 1 wins!!", 1, self.red)
                                self.screen.blit(label, (10, 10))
                                game_over = True

                    # Ask for Player 2 Input
                    else:
                        if multiplayer == 'Y':

                            posx = event.pos[0]
                            col = int(math.floor(posx / self.size))

                            if self.loc_valid(playboard, col):
                                row = self.next_row(playboard, col)
                                self.place_stone(playboard, row, col, 2)

                                if self.win_cond(playboard, 2):
                                    label = self.font.render("Player 2 wins!!", 1, self.yellow)
                                    self.screen.blit(label, (10, 10))
                                    game_over = True

                        elif multiplayer == 'N':
                            pass
                        else:
                            sys.exit()

                    self.print_board(playboard)
                    self.render_board(playboard)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(3000)


if __name__ == '__main__':
    board = PlayBoard()
    board.start_game()

import pygame
import sys
from mark import Mark
from text import TextObject
from model import TicTacToeModel
import copy
import numpy as np


class Game:
    pygame.init()
    def __init__(self,
                 caption,
                 width,
                 height,
                 frame_rate):
        pygame.init()

        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.player = -1
        #occupied doesn't really do anything anymore
        self.occupied = [0,1,2,3,4,5,6,7,8]
        #self.board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.winner = 0

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.TicTacToeModel = TicTacToeModel(9, 3, 100, 32)
        self.TicTacToeModel.load()
    def setPlayer(self):
        if self.player == -1:
            self.player = 1
        elif self.player == 1:
            self.player = -1

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)



    def checkHV(self):
        for i in range(len(self.board)):
            checking_row = self.board[i][0]
            for j in range(len(self.board[i])):
                if checking_row != self.board[i][j]:
                    checking_row = 0
            if checking_row != 0:

                return checking_row

        # Columns
        for i in range(len(self.board)):
            checking_column = self.board[0][i]
            for j in range(len(self.board[i])):
                if checking_column != self.board[j][i]:
                    checking_column = 0
            if checking_column != 0:
                return checking_column
        return 0

    def checkD(self):
        diagonal = self.board[0][0]
        for i in range(len(self.board)):
            if diagonal != self.board[i][i]:
                diagonal = 0
        if diagonal != 0:

            return diagonal

        # Second diagonal
        diagonal = self.board[0][2]
        for i in range(len(self.board)):
            if diagonal != self.board[i][len(self.board[i]) - i - 1]:
                diagonal = 0
        if diagonal != 0:
            return diagonal
        return 0



    def getAvailableMoves(self):
        availableMoves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j]) == 0:
                    availableMoves.append([i, j])
        return availableMoves

    def checkWinner(self):
        print(len(self.getAvailableMoves()))
        if self.checkHV() != 0 or self.checkD() != 0:
            if self.checkHV() != 0 :
                self.winner = self.checkHV()
            else:
                self.winner = self.checkD()
        if len(self.getAvailableMoves()) == 0:
            self.winner == 2


    def AImove(self, position):
        availableMoves = self.getAvailableMoves()
        for i in range(len(availableMoves)):
            if position[0] == availableMoves[i][0] and position[1] == availableMoves[i][1]:
                self.board[position[0]][position[1]] = 1
                if position[0] == 0 and position[1] == 0:
                    self.objects.append(Mark(300, 300, 0, 0, self.player, 30, 1))
                if position[0] == 0 and position[1] == 1:
                    self.objects.append(Mark(380, 300, 0, 0, self.player, 30, 1))
                if position[0] == 0 and position[1] == 2:
                    self.objects.append(Mark(460, 300, 0, 0, self.player, 30, 1))
                if position[0] == 1 and position[1] == 0:
                    self.objects.append(Mark(300, 380, 0, 0, self.player, 30, 1))
                if position[0] == 1 and position[1] == 1:
                    self.objects.append(Mark(380, 380, 0, 0, self.player, 30, 1))
                if position[0] == 1 and position[1] == 2:
                    self.objects.append(Mark(460, 380, 0, 0, self.player, 30, 1))
                if position[0] == 2 and position[1] == 0:
                    self.objects.append(Mark(300, 460, 0, 0, self.player, 30, 1))
                if position[0] == 2 and position[1] == 1:
                    self.objects.append(Mark(380, 460, 0, 0, self.player, 30, 1))
                if position[0] == 2 and position[1] == 2:
                    self.objects.append(Mark(460, 460, 0, 0, self.player, 30, 1))


    def handle_events(self):
        if self.winner == 0 and self.player == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if self.board[0][0] == 0:
                            self.objects.append(Mark(300, 300,0,0,self.player,30,1))
                            self.board[0][0] = -1
                            self.setPlayer()
                    elif event.key == pygame.K_2:
                        if self.board[0][1] == 0:
                            self.objects.append(Mark(380, 300, 0, 0, self.player, 30, 1))
                            self.board[0][1] = -1
                            self.setPlayer()
                    elif event.key == pygame.K_3:
                        if self.board[0][2] == 0:
                            self.objects.append(Mark(460, 300, 0, 0, self.player, 30, 1))
                            self.board[0][2] = -1
                            self.setPlayer()
                    elif event.key == pygame.K_4:
                        if self.board[1][0] == 0:
                            self.objects.append(Mark(300, 380, 0, 0, self.player, 30, 1))
                            self.board[1][0] = -1

                            self.setPlayer()
                    elif event.key == pygame.K_5:
                        if self.board[1][1] == 0:
                            self.objects.append(Mark(380, 380, 0, 0, self.player, 30, 1))
                            self.board[1][1] = -1

                            self.setPlayer()
                    elif event.key == pygame.K_6:
                        if self.board[1][2] == 0:
                            self.objects.append(Mark(460, 380, 0, 0, self.player, 30, 1))
                            self.board[1][2] = -1

                            self.setPlayer()
                    elif event.key == pygame.K_7:
                        if self.board[2][0] == 0:
                            self.objects.append(Mark(300, 460, 0, 0, self.player, 30, 1))
                            self.board[2][0] = -1

                            self.setPlayer()
                    elif event.key == pygame.K_8:
                        if self.board[2][1] == 0:
                            self.objects.append(Mark(380, 460, 0, 0, self.player, 30, 1))
                            self.board[2][1] = -1

                            self.setPlayer()
                    elif event.key == pygame.K_9:
                        if self.board[2][2] == 0:
                            self.objects.append(Mark(460, 460, 0, 0, self.player, 30, 1))
                            self.board[2][2] = -1
                            self.setPlayer()



        if self.winner == 1 or self.winner == -1:
            self.player = -1
            if self.winner == -1:
                self.objects.append(
                    TextObject(50, 650, "Player 1 wins. Press any button to close", (255, 255, 255),
                           None, 50))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        pygame.quit()
                        sys.exit()
            elif self.winner == 1:
                self.objects.append(
                    TextObject(50, 650, "Player 2 wins. Press any button to close", (255, 255, 255),
                               None, 50))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        pygame.quit()
                        sys.exit()

        if self.winner == 2:
            self.objects.append(TextObject(50, 650,"Draw. Press any button to close", (255,255,255), None, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()

        elif self.winner == 0 and self.player == 1:
            self.checkWinner()

            if self.winner == 0 and self.player == 1 and len(self.getAvailableMoves()) > 0:

                availableMoves = self.getAvailableMoves()
                maxValue = 0
                bestMove = availableMoves[0]
                for move in availableMoves:
                    boardCopy = copy.deepcopy(self.board)
                    boardCopy[move[0]][move[1]] = 1
                    value = self.TicTacToeModel.predict(boardCopy, 0)
                    if value > maxValue:
                        maxValue = value
                        bestMove = move
                selectedMove = bestMove
                self.AImove(selectedMove)
                self.setPlayer()


    def run(self):
        pygame.init()

        while not self.game_over:
            self.checkWinner()

            self.handle_events()
            self.draw()


            pygame.display.update()
            self.clock.tick(self.frame_rate)
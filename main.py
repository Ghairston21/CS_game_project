import tensorflow as tf
import os
import numpy as np
import pandas as pd
from tensorflow import keras
import pygame
from game import Game
from model_test import Game2
from model import TicTacToeModel

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TTT = Game("Tic Tac Toe", 800, 800, 60)
    TTT.TicTacToeModel.load()
    TTT.run()














# See PyCharm help at https://www.jetbrains.com/help/pycharm/

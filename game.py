import pygame
import pygame.mixer
import pygame.font
from pygame.locals import *
import math
import itertools
import sys
import thread
from time import sleep

fullscreen = False

pygame.init()

screen = pygame.display.set_mode((1280,720), fullscreen)
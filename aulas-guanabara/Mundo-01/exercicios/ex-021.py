"""
crie um programa que abra um arquivo .mp3
"""

import pygame
pygame.init()

pygame.mixer.music.load('ex-021.mp3')

pygame.mixer.music.play()
pygame.event.wait()

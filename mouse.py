# coding: utf-8

import pygame
#import de tous ce qui est local de pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#creation d'une fenetre
#Variable fenetre egal pygame.disposition.taille de la fenetre
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

#Variable pour que la fenetre ne disparait pas 
continuer = 1

#Image de fond
#variable fond egal pygame.image.charge("nom de l'image").convertir
fond = pygame.image.load("img.jpg").convert()

#Methode blit sur l'image fenetre, colle l'image fond, en commançant au coin en haut à gauche
fenetre.blit(fond, (40,30))

#Rafraichissement de l'ecran
pygame.display.flip()

#pour cela faire une boucle infini
while continuer:

#permet de mettre à jour la fenetrede pygame 
    continuer = int(input())


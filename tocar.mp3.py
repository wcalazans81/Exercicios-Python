import pygame
# O comando init() inicia o pygame
pygame.init()
# O comando mixer.music.load(arquivo de audio)carrega o audio
pygame.mixer.music.load()
# comando para dar o play
pygame.mixer.music.play()
# comando para esperar o audio tocar
pygame.event.wait()
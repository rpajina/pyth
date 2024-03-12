import pygame
from sys import exit  # importujeme si pouze exit cuz vic ze sys nepotrebujeme

pygame.init()  # spustime (inicializuje) pygame

clock = pygame.time.Clock()

# promenne na obrazovku
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode(
    (screen_width, screen_height)
)  # nastavime ze chcem obraz a jeho velikost
# prijma hodnoty v tuplu, proto (())

player_surf = pygame.image.load("cicina.png").convert_alpha()
player_x = 100
player_y = 200

monster_surf = pygame.image.load("monster_ghost.png").convert_alpha()
monster_x = 200
monster_y = 300


while True:  # piseme sem celou logiku, game loop
    for event in pygame.event.get():  # kontroluje vsechny eventy co probehly
        if event.type == pygame.QUIT:  # pro vypnuti:
            pygame.quit()  # hry
            exit()  # celyho pythonu

    key = pygame.key.get_pressed()  # promenna pro stisknutou klavesnici
    if key[pygame.K_a]:
        # if klavesa a byla stisknuta, ify jsou better bo to jde i do stran
        player_x -= 10
    if key[pygame.K_d]:  # jako bychom tam dali == True
        player_x += 10
    if key[pygame.K_w]:
        player_y -= 10
    if key[pygame.K_s]:
        player_y += 10

    screen.fill((0, 0, 0))  # prekresli obrazovku na cernou

    screen.blit(player_surf, (player_x, player_y))  # vykresli nam to ten obrazek
    screen.blit(monster_surf, (monster_x, monster_y))

    pygame.display.update()  # updatuje screen
    clock.tick(60)  # nastavujeme stejny fps na kazdym pocitaci, obnoveni 60x za sekundu

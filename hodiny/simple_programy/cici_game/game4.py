import pygame
from sys import exit  # importujeme si pouze exit cuz vic ze sys nepotrebujeme

pygame.init()  # spustime (inicializuje) pygame

clock = pygame.time.Clock()

# promenne na obrazovku
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
# nastavime ze chcem obraz a jeho velikost
# prijma hodnoty v tuplu, proto (())

def monster_animation():
    global monster_surf, monster_index #pracuje s vecma ktery jsou jinde v kodu a ne jen v ty funkci
    monster_index += 0.1

    if monster_index > len(monster_walk):
        monster_index = 0

    monster_surf = monster_walk[int(monster_index)]

player_x = 100
player_y = 200
player_surf = pygame.image.load("cicina.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
# da obrazek na obdelnik, aby to fachalo tak nemuzeme mit stejny nazvy yk

monster_x = 700
monster_y = 300

monster_walk_1 = pygame.image.load("ghost_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("ghost_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2] #ulozime obrazky pro walk do seznamu
monster_index = 0 #abyzal pak 1 hodnotu ze seznamu

monster_surf = monster_walk[monster_index] #dame aby nam bralo prvni hodnotu defaultne


monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))

lives = 3
font = pygame.font.Font(None, 25)  # vytvarime font

monster_direction = "Left"  # drzime hodnotu abychom ji pak mohli menit kdyz potrebujeme a na zaklade toho neco delat
# speed = 5

game_over = False

while True:  # piseme sem celou logiku, game loop
    for event in pygame.event.get():  # kontroluje vsechny eventy co probehly
        if event.type == pygame.QUIT:  # pro vypnuti:
            pygame.quit()  # hry
            exit()  # celyho pythonu

    if game_over == False:
        key = pygame.key.get_pressed()  # promenna pro stisknutou klavesnici
        if key[pygame.K_a]:
            # if klavesa a byla stisknuta, ify jsou better bo to jde i do stran
            player_rect.left -= 10
        if key[pygame.K_d]:  # jako bychom tam dali == True
            player_rect.right += 10
        if key[pygame.K_w]:
            player_rect.top -= 10
        if key[pygame.K_s]:
            player_rect.bottom += 10

        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 40:
            monster_direction = "Left"

        if monster_direction == "Left":
            monster_rect.x -= 5
        elif monster_direction == "Right":
            monster_rect.x += 5

        monster_animation()

        # if monster_rect.x <= 0 or monster_rect.x >= screen_width - 40:
        # speed = -speed
        # monster_rect.x += speed
        screen.fill("#000000")  # prekresli obrazovku na bilou

        text = font.render(f"Lives: {lives}", False, "#000000")
        # vytvori plochu pro text, vypppise to Lives: a akt. hodnotu zivotu
        screen.blit(text, (700, 10))

        screen.blit(player_surf, player_rect)
        # vykresli nam to ten obrazek do obdelniku pro playera
        screen.blit(monster_surf, monster_rect)

        if player_rect.colliderect(monster_rect):
            lives -= 1
        if lives <= 0:
            game_over = True
    else:
        screen.fill("#1C1B19")
        end = font.render(f"Game over", False, "#FFFFFF")
        screen.blit(end, (335, 280))
    pygame.display.update()  # updatuje screen
    clock.tick(60)  # nastavujeme stejny fps na kazdym pocitaci, obnoveni 60x za sekundu

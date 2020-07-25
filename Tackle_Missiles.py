import pygame
import random
import math
from pygame import mixer


def game_loop():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    background = pygame.image.load('./res/city_background.png')

    mixer.music.load("./res/background_game_music.wav")

    mixer.music.play(-1)

    person = pygame.image.load('./res/person.png')
    personX = 336
    personY = 480
    personX_change = 0

    missile = []
    missileX = []
    missileY = []
    missileY_change = []
    num_of_missiles = 15

    for i in range(num_of_missiles):
        missile.append(pygame.image.load('./res/missile.png'))
        missileX.append(random.randint(0, 700))
        missileY.append(-10)
        missileY_change.append(2)

    def print_person():
        screen.blit(person, (personX, personY))

    def print_missile(x, y, i):
        screen.blit(missile[i], (x, y))

    def collision_cheak(missileX, missileY, personX, personY):
        distance = math.sqrt((math.pow(missileX - personX, 2) + (math.pow(missileY - personY, 2))))

        if distance <= 27:
            return True
        else:
            return False

    game_over = pygame.font.Font('freesansbold.ttf', 45)
    fontX = 5
    fontY = 270

    def print_game_over():
        game_over_ = game_over.render("GAME OVER! Press Enter to restart", True, (0, 0, 0))
        screen.blit(game_over_, (fontX, fontY))

    score = 0
    score_font = pygame.font.Font('./res/font.ttf', 32)
    score_fontX = 10
    score_fontY = 10

    def print_score():
        score_render = score_font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_render, (score_fontX, score_fontY))

    hiscore_font = pygame.font.Font('./res/font.ttf', 32)
    hiscore_fontX = 610
    hiscore_fontY = 10

    def print_hiscore():
        hiscore_render = hiscore_font.render("Hiscore: " + str(hiscore), True, (0, 0, 0))
        screen.blit(hiscore_render, (hiscore_fontX, hiscore_fontY))

    with open("./res/Hiscore_Manager_Tackle_Missile.txt", "r") as f:
        hiscore = f.read()

    game__over = False
    running = True

    while running:
        if game__over:
            with open("./res/Hiscore_Manager_Tackle_Missile.txt", "w") as f:
                f.write(str(hiscore))
            screen.blit(background, (0, 0))
            print_game_over()
            print_hiscore()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        personX_change = 3
                    elif event.key == pygame.K_LEFT:
                        personX_change = -3

            if personX >= 736:
                game__over = True

            elif personX <= 0:
                game__over = True

            elif score > int(hiscore):
                hiscore = score
            for i in range(num_of_missiles):
                if missileY[i] >= 536:
                    score += 1
                    missileY[i] = -10
                    missileX[i] = random.randint(0, 700)
                collision = collision_cheak(missileX[i], missileY[i], personX, personY)
                if collision:
                    for j in range(num_of_missiles):
                        game__over = True

                missileY[i] += missileY_change[i]
                print_missile(missileX[i], missileY[i], i)
            print_hiscore()
            print_score()
            personX += personX_change
            print_person()
        pygame.display.update()


pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('./res/city_background.png')

mixer.music.load("./res/background_game_music.wav")

mixer.music.play(-1)

game_start = pygame.font.Font('freesansbold.ttf', 64)
fontX = 100
fontY = 270


def print_game_start():
    game_start_ = game_start.render("Press Enter to start", True, (0, 0, 0))
    screen.blit(game_start_, (fontX, fontY))


game_name = pygame.font.Font('./res/font.ttf', 45)
game_name_fontY = 100

game_name_fontX = 250


def print_game_name():
    game_name_ = game_name.render("Tackle Missiles", True, (0, 0, 0))
    screen.blit(game_name_, (game_name_fontX, game_name_fontY))


running = True

while running:
    screen.blit(background, (0, 0))
    print_game_start()
    print_game_name()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_loop()
    pygame.display.update()

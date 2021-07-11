import pygame
import random
import os
import time
pygame.mixer.init()

pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
maroon = (72, 0, 50)
purple = (33, 9, 78)

# Creating window
screen_width = 1000
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("back.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
#convert aplpha so that not take lot of processing time when replay

# Game Title
pygame.display.set_caption("SnakesGame")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 58)
font1 = pygame.font.SysFont(None, 44)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        stimg = pygame.image.load("start.png")
        stimg = pygame.transform.scale(stimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(stimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('game.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(50)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 50

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            endimg = pygame.image.load("end.png")
            endimg = pygame.transform.scale(endimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(endimg, (0, 0))
            screen_text1 = font1.render(text1, True, black)
            gameWindow.blit(screen_text1, [190,190])
            text_screen("Your Score: " + str(score), purple, 250, 450)
            text_screen("Highscore: "+str(highscore), purple, 250, 500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_t:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()
                time.sleep(0.2)
                pygame.mixer.music.load('game.mp3')
                pygame.mixer.music.play(-1)
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: "+str(highscore), maroon, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                text1 = "(You touched your tail)"
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                text1 = "(You went out of boundary)"
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play(-1)

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
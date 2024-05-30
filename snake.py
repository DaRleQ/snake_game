import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (213,5080)
green = (0,255,0)
blue = (50,153,213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game")

def draw_Snake(snake_block, snake_list):
    for element in snake_list:
        pygame.draw.rect(dis, black, [element[0], element[1], snake_block, snake_block])

def game_loop():
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_chage = 0
    y1_change = 0


    snake_block = 10
    snake_list = []
    lenght_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_chage = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_chage = 10
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_chage = 0
                    y1_change = 10
                elif event.key == pygame.K_UP:
                    x1_chage = 0
                    y1_change = -10

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        x1 += x1_chage
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        
        draw_Snake(snake_block, snake_list)
        #pygame.draw.rect(dis, black, [x1,y1, 10,10])
        pygame.display.update()
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10) * 10.0
            lenght_of_snake += 1

        time.sleep(0.1)
    pygame.quit()
    quit()

game_loop()
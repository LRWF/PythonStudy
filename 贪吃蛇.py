import sys
import pygame
import random
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('贪吃蛇 beta 1.0')

clock = pygame.time.Clock()


def main():
    fps = 10

    game_over_flag = False
    game_close = False
    eat_food = True

    screen_color = (230, 230, 250)

    score = 0

    snake_block = 10
    snake_color = (0, 0, 0)

    snake_list = []
    snake_len = 1

    snake_x = display_width / 2
    snake_y = display_height / 2

    snake_init = [snake_x, snake_y]
    snake_list.append(snake_init)

    x_change = 0
    y_change = 0

    food_block = 10
    food_color = (0, 139, 139)

    food_x = 0
    food_y = 0

    while not game_over_flag:
        while game_close:
            game_display.fill((186, 85, 211))

            msg_color = (255, 255, 255)
            message(display_width * 0.1, display_height * 0.1, 'Game Over', msg_color, 36)
            message(display_width * 0.1, display_height * 0.3, 'Press Q to quit', msg_color, 24)
            message(display_width * 0.1, display_height * 0.35, 'Press P to play', msg_color, 24)
            score_set(1, score)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over_flag = True
                        game_close = False

                    if event.key == pygame.K_p:
                        main()

                    if event.type == pygame.QUIT:
                        game_over_flag = True
                        game_close = False

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                game_over_flag = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    if y_change == 0:
                        y_change = -10

                if event.key == pygame.K_DOWN:
                    x_change = 0
                    if y_change == 0:
                        y_change = 10

                if event.key == pygame.K_LEFT:
                    if x_change == 0:
                        x_change = -10
                    y_change = 0

                if event.key == pygame.K_RIGHT:
                    if x_change == 0:
                        x_change = 10
                    y_change = 0

        if snake_x < 0 or snake_x > display_width - snake_block:
            game_close = True

        if snake_y < 0 or snake_y > display_height - snake_block:
            game_close = True

        snake_x += x_change
        snake_y += y_change

        if len(snake_list) > 2 and ([snake_x, snake_y] in snake_list):
            game_close = True

        snake_pos = [snake_x, snake_y]
        snake_list.insert(0, snake_pos)

        if [food_x, food_y] in snake_list:
            eat_food = True
            pygame.draw.rect(game_display, screen_color, (food_x, food_y, food_block, food_block))

        game_display.fill(screen_color)
        for i in snake_list:
            pygame.draw.rect(game_display, snake_color, (i[0], i[1], snake_block, snake_block))

        if eat_food:
            food_x = random.randint(food_block, display_width) // 10 * 10
            food_y = random.randint(food_block, display_height) // 10 * 10

            snake_len += 1
            score += snake_len - 2

            fps += 2
        else:
            snake_list.pop()

        pygame.draw.rect(game_display, food_color, (food_x, food_y, food_block, food_block))

        eat_food = False

        score_set(0, score)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()

    quit()


def message(x, y, msg, color, size):
    font_style = pygame.font.SysFont('微软雅黑', size)
    msg = font_style.render(msg, True, color)
    game_display.blit(msg, (x, y))


def score_set(status, n):
    if status == 0:
        score_font = pygame.font.SysFont('微软雅黑', 32)
        value = score_font.render('Your Score: ' + str(n), True, (0, 0, 0))
        game_display.blit(value, (0, 0))
    else:
        score_font = pygame.font.SysFont('微软雅黑', 24)
        value = score_font.render('Your Score: ' + str(n), True, (255, 255, 255))
        game_display.blit(value, (display_width * 0.1, display_height * 0.5))


if __name__ == '__main__':
    main()

import pygame
import time
import random
import sys

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Block size (snake segment size)
block_size = 20

# Game speed
snake_speed = 15

# Initialize display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock object to control game speed
clock = pygame.time.Clock()

# Font for score display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Display the current score on the screen"""
    value = score_font.render("Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    """Draw the snake on the screen"""
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], block_size, block_size])

def message(msg, color):
    """Display a message on the screen"""
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

def game_loop():
    """Main game loop"""
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    # Initial snake movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        # Game over screen
        while game_close:
            game_display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != block_size:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -block_size:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != block_size:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -block_size:
                    y1_change = block_size
                    x1_change = 0

        # Check if snake hits the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Drawing
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1

        # Control game speed
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    sys.exit()
    quit()
    

# Start the game
if __name__ == "__main__":
    game_loop()

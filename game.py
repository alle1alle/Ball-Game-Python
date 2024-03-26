import pygame
import sys
from ball import Ball
from paddle import Paddle
from pygame.font import Font
import random


# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Font
font = pygame.font.Font(None, 36)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Properly exit Pygame
            sys.exit()     # Exit the script

def draw_score(window, score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

def update_display():
    pygame.display.update()

def render_text(window, text, pos, color):
    font_obj = Font(None, 20)
    text_surface = font_obj.render(text, True, color)
    window.blit(text_surface, pos)

def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Ball Game")
    
    score = 0

    while True:
        handle_events()
        # Ball and paddle with values
        random_x_speed = random.uniform(-0.25, 0.25)
        ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 10, random_x_speed, 0.25)
        paddle = Paddle((WINDOW_WIDTH - 150) // 2, WINDOW_HEIGHT - 40, 150, 20)

        while True:
            handle_events()
            keys = pygame.key.get_pressed()
            paddle.move(keys, WINDOW_WIDTH)

            ball.move()
            ball.bounce_off_walls(WINDOW_WIDTH)
            if ball.bounce_off_bar(paddle.x, paddle.width, paddle.y):
                score += 1  # Increase score by 1 when the ball hits the paddle

            if ball.y >= WINDOW_HEIGHT:
                score = 0
                break

            window.fill(BLACK)
            paddle.draw(window, WHITE)
            ball.draw(window, RED)
            draw_score(window, score)

            # Render the coordinates
            ball_Xcoordinates_text = f"x: {ball.x:.0f}"
            ball_Ycoordinates_text = f"y: {ball.y:.0f}"
            render_text(window, ball_Xcoordinates_text, (10, 70), WHITE)
            render_text(window, ball_Ycoordinates_text, (10, 50), WHITE)

            update_display()

if __name__ == "__main__":
    main()
            







       

 


        

        
        








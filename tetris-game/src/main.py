import pygame
import random
from game import Game

def main():
    pygame.init()
    
    # Set up the game window
    screen_width = 300
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tetris Game")
    
    # Initialize the game
    game = Game(width=10, height=20)
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_input(event)
        
        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.delay(100)
    
    pygame.quit()

if __name__ == "__main__":
    main()
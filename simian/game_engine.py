import pygame
from simian.window.game_canvas import GameCanvas
from simian.physics.space import Size
from simian.utils.singleton import Singleton


# Game Configuration Constants
GAME_WINDOW_HEIGHT = 800
GAME_WINDOW_WIDTH = 600
GAME_NAME = "PlaceHolder Name"
NUMBER_OF_FRAMES = 60

class GameEngine(metaclass=Singleton):
    
    def load(self):
        game_window_size = Size(GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT)
        self.game_canvas = GameCanvas(game_window_size, GAME_NAME)
        

    def run(self):
        pygame.init()
        self.load()
        
        clock = pygame.time.Clock()
        self.game_canvas.open()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                else:
                    # Update Actual Game Scene 
                    pass

            # Refresh screen
            self.game_canvas.refresh_screen()

            # Set the number of frames per second
            clock.tick(NUMBER_OF_FRAMES)
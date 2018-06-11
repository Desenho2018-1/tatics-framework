from simian.object import GameObject
from simian.sprite.sprite import Sprite
from simian.input.keyboard_manager import Keyboard


class Player(GameObject):
    
    def __init__(self, x, y):
        super().__init__(x,y)
        self.sprite = Sprite("engineer.jpg")
        self.keyboard = Keyboard()
        self.speed = 500

    def update(self, time_elapsed):
        if(self.keyboard.is_key_pressed(Keyboard.RIGHT)):
            self.position.x += self.speed*time_elapsed

        if(self.keyboard.is_key_pressed(Keyboard.LEFT)):
            self.position.x -= self.speed*time_elapsed

        if(self.keyboard.is_key_pressed(Keyboard.DOWN)):
            self.position.y += self.speed*time_elapsed

        if(self.keyboard.is_key_pressed(Keyboard.UP)):
            self.position.y -= self.speed*time_elapsed
    
    def draw(self, graphics):
        self.sprite.set_x(self.position.x)
        self.sprite.set_y(self.position.y)
        graphics.add(self.sprite)

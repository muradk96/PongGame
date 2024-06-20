import pygame

class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.positionX = position_x
        self.positionY = position_y
        self.color = color
        self.radius = radius
        self.velocityX = 3
        self.velocityY = 3
        self.center = (position_x, position_y)

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.center, self.radius)

    def ball_update(self):
        self.center = (self.positionX, self.positionY)

    def move(self):

        self.positionX += self.velocityX
        self.positionY += self.velocityY

        self.ball_update()

    def wall_collision(self):
        self.velocityY *= -1

    def player_collision(self):
        self.velocityX *= -1

    def reset_position(self, window_width, window_height):
        self.positionX = window_width / 2
        self.positionY = window_height / 2
        self.velocityX *= -1

        self.ball_update()



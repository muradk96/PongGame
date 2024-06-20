import pygame


class Player:
    def __init__(self, name, position_x, position_y, color, width, height, name_position_x, name_position_y):
        self.name = name
        self.positionX = position_x
        self.positionY = position_y
        self.color = color
        self.width = width
        self.height = height
        self.rect = (position_x, position_y, width, height)
        self.rect_name = (name_position_x, name_position_y)
        self.velocity = 5
        self.font = pygame.font.Font(None, 30)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def rect_update(self):
        self.rect = (self.positionX, self.positionY, self.width, self.height)

    def move_player(self, window_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.positionY >= 0:
            self.positionY -= self.velocity

        if keys[pygame.K_DOWN] and self.positionY <= (window_height - self.height):
            self.positionY += self.velocity

        self.rect_update()


    def draw_name(self, window):
        text_surface = self.font.render(str(self.name), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect_name)

        window.blit(text_surface, text_rect)

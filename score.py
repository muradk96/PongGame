import pygame


class Score:
    def __init__(self, position_x, position_y):
        self.positionX = position_x
        self.positionY = position_y
        self.score = 0
        self.rect = (position_x, position_y)
        self.font = pygame.font.Font(None, 72)

    def draw_score(self, window):
        text_surface = self.font.render(str(self.score), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect)

        window.blit(text_surface, text_rect)

    def score_update(self):
        self.score += 1

import pygame

from player import Player
from ball import Ball
from collision_manager import CollisionManager
from score import Score

pygame.init()
window_width = 1000
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")


def redraw_window(player1, player2, ball, score_player1, score_player2):
    window.fill((0, 0, 0))
    player1.draw(window)
    player1.draw_name(window)

    player2.draw(window)
    player2.draw_name(window)

    ball.draw(window)
    pygame.draw.line(window, (255, 255, 255), (window_width / 2, 0), (window_width / 2, window_height), 5)

    score_player1.draw_score(window)
    score_player2.draw_score(window)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    player1 = Player("Murad", 10, 200, (255, 255, 255), 10, 50, 100, 50)
    player2 = Player("Amin", 980, 200, (255, 255, 255), 10, 50, 900, 50)
    score_player1 = Score(window_width / 2 - 50, 50)
    score_player2 = Score(window_width / 2 + 50, 50)

    radius = 5
    ball = Ball(window_width // 2, window_height // 2, radius, (255, 255, 255))
    collision = CollisionManager()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        player1.move_player1(window_height)
        player2.move_player2(window_height)
        ball.move()

        if collision.ball_wall_collision(ball, window_height):
            ball.wall_collision()

        if collision.ball_player1_collision(ball, player1) or collision.ball_player2_collision(ball, player2):
            ball.player_collision()

        if collision.goal_player1_collision(ball):
            score_player2.score_update()
            ball.reset_position(window_width, window_height)

        if collision.goal_player2_collision(ball, window_width):
            score_player1.score_update()
            ball.reset_position(window_width, window_height)

        redraw_window(player1, player2, ball, score_player1, score_player2)


main()

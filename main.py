import pygame

from player import Player
from collision_manager import CollisionManager
from score import Score
from network import Network
from ball import Ball

pygame.init()

window_width = 1000
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")


def read_pos(str):
    str = str.split(",")
    if len(str) == 2:
        return int(str[0]), int(str[1])
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5])


def make_pos(tup):
    input = ""
    for t in tup:
        input = input + str(t) + ","
    return input[:-1]


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

    n = Network()
    # p = n.getP()
    startPos = read_pos(n.getPos())

    player1 = Player("Murad", startPos[0], startPos[1], (255, 255, 255), 10, 50, 100, 50)
    player2 = Player("Amin", 0, 0, (255, 255, 255), 10, 50, 900, 50)

    radius = 5
    ball = Ball(window_width // 2, window_height // 2, radius, (255, 255, 255))

    score_player1 = Score(window_width / 2 - 50, 50)
    score_player2 = Score(window_width / 2 + 50, 50)

    collision = CollisionManager()

    running = True
    while running:
        clock.tick(120)
        positions = read_pos(n.send(make_pos((player1.positionX, player1.positionY, ball.positionX, ball.positionY, ball.velocityX, ball.velocityY))))
        player2.positionX = positions[0]
        player2.positionY = positions[1]
        player2.rect_update()

        ball.positionX = positions[2]
        ball.positionY = positions[3]
        ball.velocityX = positions[4]
        ball.velocityY = positions[5]

        if collision.ball_wall_collision(ball, window_height):
            ball.wall_collision()

        if collision.ball_player1_collision(ball, player1) or collision.ball_player2_collision(ball, player2):
            ball.player_collision()

        if collision.goal_player1_collision(ball):
            score_player2.score_update()
            #ball.reset_position(window_width, window_height)
            ball.velocityX *= -1

        if collision.goal_player2_collision(ball, window_width):
            score_player1.score_update()
            #ball.reset_position(window_width, window_height)
            ball.velocityX *= -1

        ball.move()

        player1.move_player(window_height)

        redraw_window(player1, player2, ball, score_player1, score_player2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


main()

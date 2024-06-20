class CollisionManager:

    def ball_player1_collision(self, ball, player1):
        if ball.positionX - ball.radius <= player1.positionX + player1.width and player1.positionY <= ball.positionY + ball.radius <= player1.positionY + player1.height:
            return True
        return False

    def ball_player2_collision(self, ball, player2):
        if ball.positionX + ball.radius >= player2.positionX and player2.positionY <= ball.positionY + ball.radius <= player2.positionY + player2.height:
            return True
        return False

    def ball_wall_collision(self, ball, window_height):
        if ball.positionY >= window_height - ball.radius or ball.positionY <= ball.radius:
            return True
        return False

    def goal_player1_collision(self, ball):
        if (ball.positionX - ball.radius) <= 0:
            return True
        return False

    def goal_player2_collision(self, ball, window_width):
        if (ball.positionX + ball.radius) >= window_width:
            return True
        return False

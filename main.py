import time
import turtle
from Snake import Snake
from Food import Food
from score import Score
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def quit():
        with open("./Score\highscore.txt") as file:
            prev_high_score = int(file.read())

        if (score.high_score > prev_high_score):
            with open("./Score\highscore.txt","w")as file:
                file.write(str(score.high_score))

        turtle.bye()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(quit, "q")


is_game_started = True



while True:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            continue
        elif snake.head.distance(segment) < 10:
            is_game_started = False
            score.reset()
            snake.reset()
  
        
        if snake.head.distance(food) < 10:

            snake.extend()
            score.increase_score()
            food.reposition()
        
screen.exitonclick()
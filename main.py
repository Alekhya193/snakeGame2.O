import turtle
from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Nokia's snake gamee")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on=True
while game_on:
 screen.update()
 time.sleep(0.1)
 snake.move()

 if snake.segments[0].distance(food) < 15:
  food.random_food()
  snake.extend()
  scoreboard.increase_score()

 if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
  scoreboard.reset()
  snake.reset()

#snake touches its own tail
 for segment in snake.segments[1:]:
  if snake.segments[0].distance(segment)<10:
   scoreboard.reset()
   snake.reset()






screen.exitonclick()
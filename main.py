
from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")

screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()


score = Turtle()

gameover = Turtle()
gameover.hideturtle()
game_is_on=True

screen.listen()

screen.onkey(snake.up,"Up")    
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

snake.speed()


def write_score(count):
    score.clear()
    score.hideturtle()
    score.penup()
    score.color("white")
    score.goto(0,260)
    score.write(f"Score : {count}", align='center', font=('Arial', 16, 'normal'))

count=0
write_score(count)
while game_is_on:
    time.sleep(0.2)
    screen.update()
    snake.move()
    if snake.collide():
        
        gameover.color("white")
        gameover.write("Game over", align='center', font=('Arial', 16, 'normal'))
        print("Collided with wall!! Game finished.")
        game_is_on = False
        
    if snake.distance(food) < 15:
        count+=1
        print("ate!!!")
        snake.grow()
        food.hideturtle()
        food = Food()
        write_score(count)
        
    
    
        
        
        
    
    

screen.exitonclick()
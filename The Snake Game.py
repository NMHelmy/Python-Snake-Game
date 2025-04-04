import time
import turtle
import random

delay = 0.1 #  delay between each drawing step, in seconds
# delay between each movement of the snake. by adjusting the value, you can make the game run slower or faster

# set up screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.penup()
head.shape("square")
head.color("Cyan")
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()

# scores
score = 0
high_score = 0

# scoreboard
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.goto(0, 260)
score_board.hideturtle()
score_board.write("Score:0 High Score:0", align= "center", font=("Courier", 24, "bold"))

segments = []
        
def snake_up():
    if head.direction != "down":
        head.direction = "up"
        
def snake_down():
    if  head.direction != "up":
        head.direction = "down"

def snake_left():
    if head.direction != "right":
        head.direction = "left"

def snake_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        y += 20
        head.sety(y)

    if head.direction == "down":
        y = head.ycor()
        y -= 20
        head.sety(y)

    if head.direction == "right":
        x = head.xcor()
        x += 20
        head.setx(x)

    if head.direction == "left":
        x = head.xcor()
        x -= 20
        head.setx(x)

screen.listen()
screen.onkeypress(snake_up, "Up")
screen.onkeypress(snake_down, "Down")
screen.onkeypress(snake_right, "Right")
screen.onkeypress(snake_left, "Left")

#time.sleep() # to reduce turtle speed

while True:
    # updating screen with any changes made sice the last update - including any movements, drawings, or other modifications to the graphics on the screen
    screen.update()

    # check collision with border
    if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1) # when this line is executed then the next line of code will be executed after 1 second
        head.goto(0,0)
        head.direction = "stop"

        # reset delay
        delay = 0.1

        # the segment needs to disappear when the snake dies
        # set the position of the segments outside the window coordinates
        # the game restarts and hence clear the segment list
        for segment in segments:
            segment.goto(1000, 1000) 
        segments.clear()

        # reset score
        score = 0
        score_board.clear()
        score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "bold"))
        
    # check collision with food
    if head.distance(food) < 20:
        X = random.randint(-280, 280)
        Y = random.randint(-280, 280)
        food.goto(X, Y)

        # add a new segment to the end
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("cyan")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay, increasing the game speed, increasing the difficulty
        delay -= 0.001 

        # increase score
        score += 10
        if score > high_score:
            high_score = score
        score_board.clear()
        score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "bold"))
    
    # moving each segment of the snake's body to the position of the segment in front of it
    for i in range(len(segments)-1, 0, -1): # loop iterates over the indices of the segments in reverse order (moving from tail to head)
        # retrieving the x and y coodinates of the segment in front of it
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        # moving the current segment to the position of the segment in front of it
        segments[i].goto(x,y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)

            for segment in segments:
                segment.goto(1000, 1000) 
            segments.clear()

            score = 0
            delay = 0.1

            score_board.clear()
            score_board.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

screen.mainloop()
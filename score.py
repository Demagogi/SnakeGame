from turtle import Turtle  # import Turtle class from turtle module


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as scr:  # reads high score stored in data.txt
            high_score = int(scr.read())  # convert string from data.txt as integer for use as score
        self.high_score = high_score  # added after update
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.screen_update()

    def screen_update(self):
        """shows score counter at the top of the screen """
        self.clear()
        arg = f"Score: {self.score} High score: {self.high_score}"
        self.write(arg=arg, move=False, align="center", font=('Arial', 16, 'normal'))

    def score_update(self):
        """updates score (increases by 1)"""
        self.score += 1
        self.screen_update()

    def reset(self):  # added after update
        """ resets the current score and if it`s highest saves it as high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:  # writes new high score to the data.txt file
                data.write(str(self.high_score))  # remakes(appends) high score integer as a string
        self.score = 0
        self.screen_update()

    # def game_over(self):  # replaced with reset after update
    #     """ moves turtle middle of the screen writes 'game over'"""
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", font=('Arial', 20, 'normal'), align="center")

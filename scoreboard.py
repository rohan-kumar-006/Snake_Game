from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        score=open(r"D:\Python Codes\Day_23_Snake Game\data.txt","r")

        self.high_score=int(score.read())
        score.close()
        self.score=0
        self.penup()
        self.goto(0,260)
        self.write(arg=f"Score:{self.score} High Score:{self.high_score}",align='center', font=('Arial', 20, 'normal'))
    
    def increase_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            score=open("D:\Python Codes\Snake Game\data.txt","w")
            score.write(str(self.high_score))
            score.close()
        self.score=0    
        self.update_score()    
         
        
    def update_score(self):
         self.clear()
         self.goto(0,260)
         self.write(arg=f"Score:{self.score} High Score:{self.high_score}",align='center', font=('Arial', 20, 'normal'))
        

    
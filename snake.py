from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
      def __init__(self):
          self.segment=[]
          self.create_snake()
          self.head=self.segment[0]

      def reset(self):
         for seg in self.segment:
            seg.goto(1000,1000)
         self.segment.clear()
         self.create_snake()
         self.head=self.segment[0]


      def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)
            
      def add_segment(self,position):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segment.append(new_segment)

               
      def extend(self):   
         #it will add new segment
         self.add_segment(self.segment[-1].position())
            

      def move(self):
        for i in range (len(self.segment)-1,0,-1):
            x_coordinate=self.segment[i-1].xcor()
            y_coordinate=self.segment[i-1].ycor()
            self.segment[i].setposition(x_coordinate,y_coordinate)
        self.head.forward(MOVING_DISTANCE)   

      #creating function for control  
      def right(self):  
        if self.head.heading()!=LEFT:
           self.head.setheading(0)
      
      def left(self):  
        if self.head.heading()!=RIGHT:
           self.head.setheading(180)

      def up(self):  
        if self.head.heading()!=DOWN:
           self.head.setheading(90)  

      def down(self):  
       if self.head.heading()!=UP:
           self.head.setheading(270)
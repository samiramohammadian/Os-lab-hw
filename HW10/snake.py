import random , arcade
from arcade.key import DOWN, LEFT, RIGHT

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

############################################################################################################

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 16
        self.height = 16
        self.color = arcade.color.BLACK
        self.body_size = 0
        self.body = []
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.speed = 4
        self.change_x = 0 
        self.change_y = 0
    
    def eat(self ,a):
        if a== 1:
            self.body_size +=1
        elif a == 2:
            self.body_size +=2
        elif a == 3:
            self.body_size -=1
            if self.body_size == -1 :
                exit()


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , self.color)
        for i,part in enumerate (self.body) :
            arcade.draw_rectangle_filled(part[0] , part[1] , self.width , self.height , self.color)
            

    def move(self):
        self.body.append([self.center_x , self.center_y])

        if len(self.body) > self.body_size :
            self.body.pop(0)

        if self.change_x == -1 :
            self.center_x -= self.speed
        elif self.change_x == 1 :
            self.center_x += self.speed

        if self.change_y == -1 :
            self.center_y -= self.speed
        elif self.change_y == 1 :
            self.center_y += self.speed

        if self.center_y < 0   or  self.center_y > 500 : 
            arcade.start_render()
            text = "GAME OVER"
            arcade.draw_text(text, 250, 250, arcade.color.RED, 50, anchor_x='center')
            arcade.finish_render()
            exit()
            
        
        if self.center_x < 0   or  self.center_x > 500 : 
            arcade.start_render()
            text = "GAME OVER"
            arcade.draw_text(text, 250, 250, arcade.color.RED, 50, anchor_x='center')
            arcade.finish_render()
            exit()

####################################################################################################################################
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height =16 
        self.color = arcade.color.RED
        self.r = 8
        self.center_x = random.randint(0 , SCREEN_WIDTH-1)
        self.center_y = random.randint(0 , SCREEN_HEIGHT-1)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )

#####################################################################################################################################
class Pear(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height =16 
        self.color = arcade.color.YELLOW
        self.r = 8
        self.center_x = random.randint(0 , SCREEN_WIDTH-1)
        self.center_y = random.randint(0 , SCREEN_HEIGHT-1)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )

#########################################################################################################################################
class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height =16 
        self.color = arcade.color.DARK_BROWN
        self.r = 8
        self.center_x = random.randint(0 , SCREEN_WIDTH-1)
        self.center_y = random.randint(0 , SCREEN_HEIGHT-1)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )

#########################################################################################################################################

class Game_screen(arcade.Window):

    def __init__(self):
        super().__init__(width=500 , height=500 , title="__SNAKE GAME__")
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.snake = Snake()
        self.apple = Apple()
        self.pear  = Pear()
        self.poop  = Poop()
        self.SCORE =0 


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        txt = "score : " 
        arcade.draw_text(txt + str(self.SCORE),  0 , 470 , arcade.color.BLACK , 15 , anchor_x='left')


    def on_update(self, delta_time: float):
        self.snake.move()
        

        if arcade.check_for_collision(self.snake , self.apple):
            self.snake.eat(1)
            self.apple = Apple()
            self.SCORE += 1

        elif arcade.check_for_collision(self.snake , self.pear):
            self.snake.eat(2)
            self.pear = Pear()
            self.SCORE += 2

        elif arcade.check_for_collision(self.snake , self.poop):
            self.snake.eat(3)
            self.poop = Poop()
            self.SCORE -=1
        

    def on_key_release(self, key: int, modifiers: int):

        if key == arcade.key.LEFT :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT :
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif  key == arcade.key.UP :
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN :
            self.snake.change_y = -1
            self.snake.change_x = 0

        
###########################################################################################################################################

my_game = Game_screen()
arcade.run()

    
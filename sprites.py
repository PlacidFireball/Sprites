import random

class Sprite: 
    def __init__(self, width=0, height=0, loc=(0, 0), direction=(0, 0), content=None): 
        self.width = width # I think that this is self explanatory
        self.height = height
        self.location = loc
        self.content = content
        self.score = 0
        self.dir = direction
    
    def locate(self, x=0, y=0, change=False): 
        """method used to change the location of the Sprite, returns a location if change is False
        otherwise, it sets the location based on a provided x and y"""
        if not change: 
            return self.location
        self.location = (x, y)
    
    def move(self, dx=0, dy=0):
        """writer method that changes location in a smoother fashion"""
        x = dx + self.location[0]
        y = dy + self.location[1]
        self.location = (x, y)
    
    def bounce(self, other, size):
        """bounds the Sprite to the screen and checks if the Sprite has 
        collided with another sprite, if it has"""
        self.bound(size)
        if self.collision(other):
            dx, dy = self.get_dir()
            self.set_dir(-dx, dy)

    def rand_dir(self):
        """used specifically for the ball in pong.py, not useful otherwise, use
        set_dir() instead of this guy"""
        direction = random.choice([-1, 1])
        x = random.randint(3, 5)
        y = random.randint(1, 3)
        self.dir = (direction*x, direction*y)

    def get_dir(self):
        """simple reader method to return the direction of the sprite"""
        return self.dir
    
    def set_dir(self, dx, dy):
        """simple writer method to set the direction"""
        self.dir = (dx, dy)

    def get_content(self): 
        return self.content

    def set_content(self, content):
        self.content = content
    
    def get_dim(self):
        """helper method, returns x, y, x+width, y+height in a tuple"""
        return self.location[0], self.location[1], self.location[0]+self.width, self.location[1]+self.height

    def bound(self, size, other=None):
        """method that keeps sprite within window."""
        x, y, rx, by = self.get_dim()
        dx, dy = self.get_dir()
        if x < 0: 
            x = 0
            self.set_dir(-dx, dy)
            self.locate(x, y, change=True)
        if y < 0: 
            y = 0
            self.set_dir(dx, -dy)
            self.locate(x, y, change=True)    
        if rx >= size[0]: 
            x = size[0] - self.width - 1
            self.set_dir(-dx, dy)
            self.locate(x, y, change=True)      
        if by >= size[1]: 
            y = size[1] - self.height - 1
            self.set_dir(dx, -dy)
            self.locate(x, y, change=True) 
            
    def collision(self, other): 
        """method that tests if two Sprites have 'collided'"""
        x, y, rx, by = self.get_dim()
        _x, _y, _rx, _by = other.get_dim()
        return x <= _rx and y <= _by and rx >= _x and by >= _y
    
    def get_score(self):
        """simple reader method that returns self.score"""
        return self.score

    def score_plus_one(self):
        """simple writer method that adds one to self.score"""
        self.score += 1
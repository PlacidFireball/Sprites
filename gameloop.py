import pygame

_running = True
screen_size = (1024, 720) # screen size is 1024x720 pixels

def on_init():
    # things you want to happen before the game starts
    pygame.init()
    display_surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF) # make the screen
    if False: # if something goes wrong, don't start the game
        return False
    return True # otherwise proceed as normal

def on_event(event): # handling pygame events
    if event.type == pygame.QUIT: # if the game is closed
        global _running 
        _running = False

def on_loop(): # handling game logic, like movement
    pass 

def on_render(): # handling actual rendering of objects (like our Sprite)
    pass 

def on_cleanup(): # when the game is done, close pygame
    pygame.quit()


if not on_init():
    global _running
    _running = False 
        
while( _running ): # the main game loop
    for event in pygame.event.get(): # event handling
        on_event(event)
    on_loop()
    on_render()
on_cleanup()





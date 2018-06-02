from microbit import *
import random

display.scroll("Get ready...")

# Game constants - These variables have capitalised names to suggest that they are not supposed to be edited. (They store constants)
DELAY =                       # ms between each frame
FRAMES_PER_WALL_SHIFT =       # number of frames between each time a wall moves a pixel to the left
FRAMES_PER_NEW_WALL =        # number of frames between each new wall
FRAMES_PER_SCORE =            # number of frames between score rising by 1
SPEED_WHEN_FLAPPING = -8        # you'll see ;)
TERMINAL_VELOCITY = 2

# Global variables - Variable scopes that allow unrestricted access throughout the code. In Python functions, these are accessed by running 'global <variable_name>'
y = 
speed = 
score = 
frame = 

# Make an image that represents a pipe to dodge
def make_pipe():
    pipe = Image("00003:00003:00003:00003:00003")
    gap = random.randint(0,3)       # random position on the wall
    # note: set_pixel() takes in the X position, the Y position and the BRIGHTNESS that you want at the pixel.
    pipe.set_pixel(4, gap, 0)       # generate a hole in the pipe at that position by removing its brightness.
    # how can I make the gap 2 pixels tall?
    return pipe
    
# create first pipe
pipe = make_pipe() # note that while this pipe does CONTAIN the SAME VALUE as the above pipe, it is NOT the SAME VARIABLE.

# Game loop
while True:
    display.show(pipe)
    
    # flap (negative velocity is upward) if button a was pressed
    if button_a.was_pressed():
        speed = SPEED_WHEN_FLAPPING
        
    # accelerate down to terminal velocity
    speed = speed + 1
    if speed > TERMINAL_VELOCITY: # I don't want to exceed my terminal velocity.
        speed = TERMINAL_VELOCITY
        
    # limits the y position of the bird
    y += speed
    if y > 99: # I don't want to exceed 99.
        y = 
    if y < 0: # I don't want to go below 0.
        y = 
        
    # draw bird
    bird_y = int(y / 20) # type conversion to integer
    display.set_pixel(1, bird_y, 9) # only the pipes move to the left, the bird remains on the x=1 column.
    
    # check for collision
    if pipe.get_pixel(1, bird_y) != 0:
        # end the game
    
    # move wall left
    if(frame % FRAMES_PER_WALL_SHIFT == 0):
        # what do I do here?
    
    # create new wall
    if(frame % # oops. I forgot what to type here. Help me fill this in!:
        # again, what do I do here?
        
    # increase score
    if # oops again! I spilled water on my keyboard! what should I type here?
        score += 1 # score = score + 1
    
    # wait 20ms
    # increase the frame count!
    
